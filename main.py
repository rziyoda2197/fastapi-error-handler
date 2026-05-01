from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    try:
        # Userlar ro'yxatidan user_id ga mos user qidirish
        user = {"id": 1, "name": "John Doe", "email": "john@example.com"}
        if user_id != user["id"]:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        # Xatolik yuz berishi uchun xatolikni qaytarish
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/users/{user_id}/email")
async def get_user_email(user_id: int):
    try:
        # Userlar ro'yxatidan user_id ga mos user qidirish
        user = {"id": 1, "name": "John Doe", "email": "john@example.com"}
        if user_id != user["id"]:
            raise HTTPException(status_code=404, detail="User not found")
        return {"email": user["email"]}
    except Exception as e:
        # Xatolik yuz berishi uchun xatolikni qaytarish
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/users/{user_id}/name")
async def get_user_name(user_id: int):
    try:
        # Userlar ro'yxatidan user_id ga mos user qidirish
        user = {"id": 1, "name": "John Doe", "email": "john@example.com"}
        if user_id != user["id"]:
            raise HTTPException(status_code=404, detail="User not found")
        return {"name": user["name"]}
    except Exception as e:
        # Xatolik yuz berishi uchun xatolikni qaytarish
        raise HTTPException(status_code=500, detail="Internal Server Error")
