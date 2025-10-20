import pytest
import requests

#CRUD
BASE_URL = "http://localhost:5000"
tasks = []

def test_create_task():
    new_task_data = {
        "title": "Test Task",
        "description": "This is a test task"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Task created"
    assert "id" in response.json()
    tasks.append(response.json()["id"])

def test_read_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    data = response.json()
    assert "tasks" in data
    assert "total" in data
    assert data["total"] >= 1

def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json['id']

def get_task():
    if tasks:
        return tasks[0]
    return None