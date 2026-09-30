from fastapi import FastAPI

app = FastAPI(title="Sample API")

items = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Mouse", "price": 24.99},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}


@app.get("/items")
def get_items():
    return items


# TODO: Add POST /items
# TODO: Add GET /items/{item_id}
# TODO: Add PUT /items/{item_id}
# TODO: Add DELETE /items/{item_id}
