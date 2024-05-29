from http.client import HTTPException
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, field_validator, ValidationError, constr

app = FastAPI()


class Task(BaseModel):
    id: int
    name: constr(pattern=r"^[a-zA-Z]+$")
    description: constr(min_length=4, max_length=12)
    is_done: bool

    @field_validator('id')
    def check_id(cls, id):
        if id <= 0:
            raise ValueError('error')
        return id


tasks = {1:Task(**{'id': 1, 'name': 'learn', 'description': 'to python', 'is_done': True}),2:Task(**{'id': 2, 'name': 'game', 'description': 'shachmat', 'is_done': False})}


@app.get("/")
async def getTasks():
    return tasks


@app.get("/{id}")
async def getTask(t_id):
    return [t for t in tasks if t.id == int(t_id)]


@app.post("/task/")
async def add_task(task: Task):
    try:
        tasks.append(Task(task.dict()))
    except ValidationError:
        raise HTTPException(status_code=400, detail="error occurred")
    return task


@app.put("/{t_id}/")
async def update_task(t_id, task: Task):
    try:
        t1 = [t for t in tasks if t.id == int(t_id)]
        t1=Task(t1)
        t1.id = task.name
        t1.description = task.description
        t1.if_done = task.if_done
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return task


@app.delete("/{t_id}/")
async def delete_task(t_id):
    try:
        t1 = [t for t in tasks if t['id'] == int(t_id)]
        tasks.remove(t1)
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return t_id


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8080)

