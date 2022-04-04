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


def update(task_id: int, text: str) -> None:
    pass

def update_status_entry(task_id: int, text: str) -> None:
    pass

def insert_new_task(text: str) ->  int:
    conn = db.connect()
    print("Within db")
    query = 'INSERT INTO UserProfile (userFirstName, userLastName, destinationCity, email, password) VALUES ("Steven", "James", "New York City", "e12", "pass");'
    conn.execute(query)
    task_id = 2
    # query_results = conn.execute("SELECT * FROM UserProfile ORDER BY userLastName DESC LIMIT 1;")
    # print("Here1")
    # query_results = [x for x in query_results]
    # print("Here2")
    # task_id = query_results[0][0]
    # print("Here3")
    conn.close()

    return task_id

def remove_task_by_id(task_id: int) -> None:
    conn = db.connect()
    query = 'DELETE FROM UserProfile WHERE email="e";'
    conn.execute(query)
    task_id = 2
    conn.close()

def search_db() -> None:
    conn = db.connect()
    query = 'SELECT * FROM CountryData WHERE country="Iraq";'
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