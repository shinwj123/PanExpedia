from app import db
from datetime import date, timedelta

curr_search = []

def fetch_todo() -> dict:
    # """Reads all tasks listed in the todo table

    # Returns:
    #     A list of dictionaries
    # """
    #return todo_list

    conn = db.connect()
    #query = 'INSERT INTO UserProfile (userFirstName, userLastName, destinationCity, email, password) VALUES ("{}", "{}", "Chicago", "email", "pass");'
    #conn.execute(query)
    query = conn.execute("Select * from UserProfile;").fetchall()
    conn.close()

    users = []
    for result in query:
        item = {
            "id": result[3],
            "task": result[2],
            "status": "Todo"
        }
        users.append(item)
    return users


def update(fn: str, ln: str, dc: str, email: str, p: str) -> None:
    conn = db.connect()
    # Get original city for validation purposes
    query = 'SELECT destinationCity FROM UserProfile WHERE email="{}"'.format(email)
    results = conn.execute(query)
    cities = []
    for r in results:
       item = {
           "city": r[0]
       }
       cities.append(item)
    original_city = cities[0]["city"]
    # query = '''CREATE TRIGGER UpdateCityTrigger
    #              BEFORE UPDATE ON UserProfile
    #              FOR EACH ROW
    #              BEGIN
    #                SET @city = (SELECT airportCity FROM AirportData WHERE airportCity = new.destinationCity );
    #              IF @city IS NOT NULL THEN
    #                SET new.destinationCity = new.destinationCity;
    #              ELSE
    #                SET new.destinationCity = old.destinationCity;
    #              END IF;
    #              END; 
    #              '''
    query2 = 'UPDATE UserProfile SET userFirstName="{}", userLastName="{}", destinationCity="{}", password="{}" WHERE email="{}";'.format(fn, ln, dc, p, email)
    conn.execute(query2)
    results = conn.execute(query)
    cities = []
    for r in results:
        item = {
            "city": r[0]
        }
        cities.append(item)
    new_city = cities[0]["city"]
    conn.close()
    return original_city, new_city

def insert_new_user(fn: str, ln: str, dc: str, email: str, p: str) ->  int:
    conn = db.connect()
    query = 'INSERT INTO UserProfile (userFirstName, userLastName, destinationCity, email, password) VALUES ("{}", "{}", "{}", "{}", "{}");'.format(fn, ln, dc, email, p)
    conn.execute(query)
    task_id = 2
    conn.close()

    return task_id

def remove_user_by_email(email: str) -> None:
    conn = db.connect()
    query = 'DELETE FROM UserProfile WHERE email="'+email+'";'
    conn.execute(query)
    conn.close()

def search_db(c: str) -> None:
    conn = db.connect()
    query = '''SELECT * 
               FROM CountryData 
               WHERE country LIKE "%%{}%%";'''.format(c)
    results = conn.execute(query)
    conn.close()
    res = []
    for r in results:
        item = {
            "country": r[0],
            "population": r[2]
        }
        res.append(item)
        curr_search.append(r[0])

    return res

def search_country(c: str):
    curr_search.clear()
    # Country Name and Population
    country_res = search_db(c)
    # Get airport data from Country if exists
    conn = db.connect()
    query = 'select CASE WHEN count(1) > 0 THEN "true" ELSE "false" END from AirportData where country LIKE "%%{}%%"'.format(c)
    results = conn.execute(query)
    res = []
    for r in results:
        item = {
            "airport_exists": r[0]
        }
        res.append(item)
    airport_exists = res[0]["airport_exists"]
    if (airport_exists):
        query = 'SELECT airportName, airportCode FROM AirportData WHERE country LIKE "%%{}%%"'.format(c)
        results = conn.execute(query)
        airport_res = []
        for r in results:
            item = {
                "airport_name": r[0],
                "airport_code": r[1]
            }
            airport_res.append(item)
        
    # # Get Covid Data
    # d = date.today() - timedelta(days=2)
    # d = '2022-03-15'
    # query = 'SELECT newCaseNumber FROM CovidCases WHERE country = "{}" AND date="{}";'.format(c, d)
    # results = conn.execute(query)
    # covid_res = []
    # for r in results:
    #     item = {
    #         "covid_cases": r[0]
    #     }
    #     covid_res.append(item)

    # Get Vaccination Rate
    query = 'SELECT SUM(population) FROM CountryData WHERE country LIKE "%%{}%%" '.format(c)    
    results = conn.execute(query)
    query1 = 'SELECT SUM(newCaseNumber) FROM CovidCases WHERE country LIKE "%%{}%%" '.format(c)
    results1 = conn.execute(query1)
    rates = []
    rates1 = []
    for r in results:
        rates.append(r[0])

    for r in results1:
        rates1.append(r[0])
    
    rate = round(float(rates1[0]/rates[0]), 5)
    conn.close()
    return country_res, airport_res, rate

def getCovidRate():
    conn = db.connect()
    query = 'SELECT country, SUM(newCaseNumber)/population as rate FROM CountryData NATURAL JOIN CovidCases GROUP BY country ORDER BY rate DESC;'
    results = conn.execute(query)
    conn.close()
    res = []
    for r in results:
        if(r[0] in curr_search):
            item = {
                "country": r[0],
                "rate": r[1]
            }
            res.append(item)

    return res

def getVaxRate():
    conn = db.connect()
    query = 'SELECT airportName as "Airport", country as "Country", rate/3 as "Vaccination Rate" FROM (SELECT country as c, SUM(dailyVaccinationNumber)/population as rate FROM CountryData NATURAL JOIN Vaccination GROUP BY country) as temp, AirportData WHERE rate > 0.5 AND country = c;'
    results = conn.execute(query)
    conn.close()
    res = []
    for r in results:
        item = {
            "airport": r[0],
            "country": r[1],
            "vaccinationRate": r[2]
        }
        res.append(item)

    return res

def login(email: str, p: str):
    conn = db.connect()
    query = 'select CASE WHEN count(1) > 0 THEN "true" ELSE "false" END from UserProfile where email = "{}"'.format(email)
    results = conn.execute(query)
    conn.close()
    res = []
    for r in results:
        item = {
            "email_exists": r[0]
        }
        res.append(item)
    #valid = results[0][0]
    v = res[0]["email_exists"]
    valid = False
    if (v == 'true'):
        conn = db.connect()
        query = 'SELECT password FROM UserProfile WHERE email="{}"'.format(email)
        results = conn.execute(query)
        conn.close()
        res = []
        for r in results:
            item = {
                "pass": r[0]
            }
            res.append(item)
        if (res[0]["pass"] == p):
            valid = True
        else:
            #print("HERE")
            valid = False
    else:
        return valid
    #print("VALID: " + str(valid))
    return valid

def getmoreinfo():
    
    conn = db.connect()
    query = 'call CountrySummary();'
    results = conn.execute(query)
    conn.close()
    res = []
    for r in results:
        if(r[0] in curr_search):

            item = {
                "country": r[0],
                "vaccrate": r[1],
                "deathcaserate": r[2]
            }
            res.append(item)

    return res

def getDestinationCity(email):
    
    conn = db.connect()
    query = 'SELECT destinationCity FROM UserProfile WHERE email="{}"'.format(email)
    results = conn.execute(query)
    conn.close()
    res = []
    
    for r in results:
        item = {
            "destinationcity": r[0]
        }
        
        res.append(item)
    
    city = res[0]["destinationcity"]

    return city