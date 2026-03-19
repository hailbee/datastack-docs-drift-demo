from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI(
    title="DataStack Demo API",
    version="1.1.0",
    description="Demo API for docs drift automation."
)


class CreateUserRequest(BaseModel):
    email: EmailStr
    full_name: str
    plan: str = "free"


class UserResponse(BaseModel):
    id: str
    email: EmailStr
    full_name: str
    plan: str


class PurchaseResponse(BaseModel):
    purchase_id: str
    status: str
    amount_cents: int
    currency: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/users", response_model=UserResponse)
def create_user(payload: CreateUserRequest):
    return {
        "id": "usr_123",
        "email": payload.email,
        "full_name": payload.full_name,
        "plan": payload.plan,
    }


@app.get("/purchases/{purchase_id}", response_model=PurchaseResponse)
def get_purchase(purchase_id: str):
    if purchase_id == "missing":
        raise HTTPException(status_code=404, detail="Purchase not found")
    return {
        "purchase_id": purchase_id,
        "status": "processed",
        "amount_cents": 2599,
        "currency": "USD",
    }