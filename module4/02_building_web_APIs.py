"""
LESSON 2: Building Web APIs with FastAPI
FastAPI allows you to turn your Python functions into HTTP Web Services in seconds.
Run using: uvicorn 02_building_web_apis:app --reload
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Our Group Learning API")

# Temporary in-memory database
tasks = [
    {"id": 1, "title": "Finish Module 1", "completed": True},
    {"id": 2, "title": "Build Web Scraping Bot", "completed": False}
]

# Data validation model
class Task(BaseModel):
    title: str
    completed: bool = False

@app.get("/")
def home():
    """Root endpoint returning basic welcome metadata."""
    return {"status": "Online", "message": "Welcome to our FastAPI server!"}

@app.get("/tasks")
def get_all_tasks():
    """Endpoint returning all stored tasks."""
    return {"total": len(tasks), "data": tasks}

@app.post("/tasks")
def create_task(new_task: Task):
    """Endpoint allowing users to add a new task."""
    task_dict = new_task.dict()
    task_dict["id"] = len(tasks) + 1
    tasks.append(task_dict)
    return {"message": "Task created successfully!", "task": task_dict}

# Note: Run this script via terminal: uvicorn 02_building_web_apis:app --reload
