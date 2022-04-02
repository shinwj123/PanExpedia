def fetch_todo() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """

    todo_list = [
        {
            "id": 1,
            "task": "test1",
            "stauts": "Todo"
        },
        {
            "id": 1,
            "task": "test1",
            "stauts": "Todo"
        },
    ]

    return todo_list

def update_task_entry(task_id: int, text: str) -> None:
    pass

def update_status_entry(task_id: int, text: str) -> None:
    pass

def insert_new_task(text: str) ->  int:
    pass


def remove_task_by_id(task_id: int) -> None:
    pass