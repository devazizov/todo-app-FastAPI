import uvicorn
from fastapi import FastAPI
from routes import index_router, todo_router
from database.config import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(index_router)
app.include_router(todo_router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True)