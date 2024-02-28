from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

tasks = [
    {"id": 1, "title": "Task 1", "description": "Description 1", "completed": False},
    {"id": 2, "title": "Task 2", "description": "Description 2", "completed": True},
]


class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool


@app.get("/tasks")
async def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks")
async def create_task(task: Task):
    tasks.append(task.dict())
    return {"status": "Task updated"}


@app.put("/tasks/{task_id}")
async def update_task(task_id: int, updated_task: Task):
    for task in tasks:
        if task["id"] == task_id:
            tasks.update(updated_task.dict())
            return {"status": "Task updated"}
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"status": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")