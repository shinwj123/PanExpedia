from app import db

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
    print("hereeee")
    print(fn)
    print(email)
    query = '''CREATE TRIGGER UpdateTrig
                 BEFORE UPDATE ON UserProfile
                 FOR EACH ROW
                 BEGIN
                   SET @city = (SELECT airportCity FROM AirportData WHERE airportCity = new.destinationCity );
                 IF @city IS NULL THEN
                   SET new.destinationCity = "INVALID";
                 END IF;
                 END; 
                 '''
    #results = conn.execute(query)
    query = 'UPDATE UserProfile SET userFirstName="{}", userLastName="{}", destinationCity="{}", password="{}" WHERE email="{}";'.format(fn, ln, dc, p, email)
    print(query)
    results = conn.execute(query)
    conn.close()
    print(results)
    return results


def insert_new_user(fn: str, ln: str, dc: str, email: str, p: str) ->  int:
    print("HEHEHEHE")
    conn = db.connect()
    print("Within db")
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

    return res

def getCovidRate():
    conn = db.connect()
    query = 'SELECT country, SUM(newCaseNumber)/population as rate FROM CountryData NATURAL JOIN CovidCases GROUP BY country ORDER BY rate DESC;'
    results = conn.execute(query)
    conn.close()
    res = []
    for r in results:
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
            valid = False

    return valid
    
def search_country(c: str):
    res = search_db(c)
    return res