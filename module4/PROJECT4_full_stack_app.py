"""
MODULE 4 CAPSTONE PROJECT: Full-Stack Project API Service
Instructions: Run this script with python or uvicorn to launch a REST API server
that manages projects, computes metrics, and persists data.
"""

import json
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="Capstone Course Hub API",
    description="Full-stack API to track learning modules, projects, and group member progress."
)

DATA_FILE = "projects_db.json"

class ProjectItem(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    module_number: int
    tech_stack: List[str]

def load_db():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.get("/")
def index():
    return {
        "status": "Active",
        "system": "Python Course Capstone Engine",
        "docs_url": "http://127.0.0.1:8000/docs"
    }

@app.get("/projects", response_model=List[ProjectItem])
def list_projects(module: Optional[int] = None):
    projects = load_db()
    if module is not None:
        return [p for p in projects if p["module_number"] == module]
    return projects

@app.post("/projects", status_code=201)
def add_project(project: ProjectItem):
    db = load_db()
    project_data = project.dict()
    project_data["id"] = len(db) + 1
    db.append(project_data)
    save_db(db)
    return {"message": "Project registered successfully!", "project": project_data}

@app.get("/projects/{project_id}")
def get_project(project_id: int):
    db = load_db()
    for p in db:
        if p["id"] == project_id:
            return p
    raise HTTPException(status_code=404, detail="Project not found")

"""
HOW TO RUN THIS CAPSTONE API:
1. In terminal, run: uvicorn project_full_stack_app:app --reload
2. Open your web browser to http://127.0.0.1:8000/docs
3. Interactive API documentation (Swagger UI) lets you test all GET and POST routes live!
"""
