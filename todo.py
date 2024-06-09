from fastapi import APIRouter, Path, HTTPException
from model import Todo

todo_router = APIRouter()

todo_list = []
current_id = 1

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    global current_id
    todo_with_id = {**todo.dict(), "id": current_id}
    todo_list.append(todo_with_id)
    current_id += 1
    return {
        "msg": "todo added successfully",
        "todo": todo_with_id
    }

@todo_router.get("/todo")
async def retrieve_todos() -> list:
    return todo_list

@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve")) -> dict:
    for todo in todo_list:
        if todo["id"] == todo_id:
            return {"todo": todo}
    raise HTTPException(status_code=404, detail="Todo with supplied ID doesn't exist")

@todo_router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int = Path(..., title="The ID of the todo to delete")) -> dict:
    global todo_list
    todo_list = [todo for todo in todo_list if todo["id"] != todo_id]
    return {
        "msg": "Todo deleted successfully"
    }
