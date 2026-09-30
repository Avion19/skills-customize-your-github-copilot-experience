from fastapi import FastAPI

app = FastAPI(title="To-Do API")

# In-memory list of tasks
items = [
    {"id": 1, "title": "Write code", "done": False},
    {"id": 2, "title": "Study for test", "done": True},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the To-Do API!"}


@app.get("/tasks")
def get_tasks():
    return items


# TODO: Add POST /tasks to create a new task
# TODO: Add GET /tasks/{task_id} to get one task
# TODO: Add PUT /tasks/{task_id} to update a task
# TODO: Add DELETE /tasks/{task_id} to remove a task
