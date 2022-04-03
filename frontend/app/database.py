from app import db

def fetch_todo() -> dict:
    # """Reads all tasks listed in the todo table

    # Returns:
    #     A list of dictionaries
    # """

    todo_list = [
        {
            "id": 1,
            "task": "test1",
            "status": "Todo"
        },
        {
            "id": 1,
            "task": "test1",
            "status": "Todo"
        },
    ]

    #return todo_list

    conn = db.connect()
    #query = 'INSERT INTO UserProfile (userFirstName, userLastName, destinationCity, email, password) VALUES ("{}", "{}", "Chicago", "email", "pass");'
    #conn.execute(query)
    query = conn.execute("Select * from UserProfile;").fetchall()
    conn.close()
    users = []
    for result in query:
        item = {
            "id": result[0] + " " + result[1],
            "task": result[2],
            "status": "Todo"
        }
        todo_list.append(item)
    return todo_list


def update_task_entry(task_id: int, text: str) -> None:
    pass

def update_status_entry(task_id: int, text: str) -> None:
    pass

def insert_new_task(text: str) ->  int:
    conn = db.connect()
    query = 'INSERT INTO UserProfile (userFirstName, userLastName, destinationCity, email, password) VALUES ("{}", "{}", "Chicago", "email", "pass");'.format(text, text)
    con.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()

    return task_id

def remove_task_by_id(task_id: int) -> None:
    pass