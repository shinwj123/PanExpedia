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
    query = 'UPDATE UserProfile SET userFirstName="'+fn+'", userLastName="'+ln+'", destinationCity="'+dc+'", password="'+p+'" WHERE email="'+email+'";'.format(fn, ln, dc, p, email)
    #query = 'UPDATE UserProfile SET userFirstName="steven", userLastName="james", destinationCity="Chicago", password="asdf" WHERE email="tejal";'
    print("ARE YOU THERE")
    conn.execute(query)
    conn.close()

def update_status_entry(task_id: int, text: str) -> None:
    pass

def insert_new_user(fn: str, ln: str, dc: str, email: str, p: str) ->  int:
    conn = db.connect()
    print("Within db")
    query = 'INSERT INTO UserProfile (userFirstName, userLastName, destinationCity, email, password) VALUES ("{}", "{}", "{}", "{}", "{}");'.format(fn, ln, dc, email, p)
    conn.execute(query)
    task_id = 2
    conn.close()

    return task_id

def remove_task_by_id(task_id: int) -> None:
    conn = db.connect()
    query = 'DELETE FROM UserProfile WHERE email="email";'
    conn.execute(query)
    task_id = 2
    conn.close()

def search_db(c: str) -> None:
    conn = db.connect()
    print(c)
    query = 'SELECT * FROM CountryData WHERE country="{}";'.format(c)
    results = conn.execute(query)
    conn.close()
    res = []
    for r in results:
        item = {
            "country": r[0],
            "population": r[2]
        }
        res.append(item)
    print("SUCCESS!")
    print(res)

    return res