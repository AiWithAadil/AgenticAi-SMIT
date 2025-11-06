from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.db import (
    create_advice,
    get_all_advices,
    get_advice_by_id,
    get_advice_by_category,
    update_advice,
    delete_advice
)

app = FastAPI(title="Advice API")

# ----------------------------
# Pydantic model for input validation
# ----------------------------
class Advice(BaseModel):
    title: str
    description: str
    category: str


# ----------------------------
# Routes
# ----------------------------

@app.get("/")
def home():
    return {"message": "Welcome to Advice API 🚀"}


# Create
@app.post("/advices/")
def create_advice_route(advice: Advice):
    return create_advice(advice.title, advice.description, advice.category)


# Read all
@app.get("/advices/")
def get_all_advices_route():
    return get_all_advices()


# Read by ID
@app.get("/advices/{advice_id}")
def get_advice_by_id_route(advice_id: int):
    return get_advice_by_id(advice_id)


# Read by category
@app.get("/advices/category/{category}")
def get_advice_by_category_route(category: str):
    return get_advice_by_category(category)


# Update
@app.put("/advices/{advice_id}")
def update_advice_route(advice_id: int, advice: Advice):
    return update_advice(advice_id, advice.title, advice.description, advice.category)


# Delete
@app.delete("/advices/{advice_id}")
def delete_advice_route(advice_id: int):
    return delete_advice(advice_id)
