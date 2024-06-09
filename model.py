from pydantic import BaseModel

class Todo(BaseModel):
    author: str
    item: str
    time: str
