from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    description: str | None = None
    done: bool = False


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    pass


class TodoInDB(TodoBase):
    id: int

    class Config:
        from_attributes = True


class Todo(TodoInDB):
    pass
