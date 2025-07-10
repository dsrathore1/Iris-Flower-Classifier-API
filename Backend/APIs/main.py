from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class Message(BaseModel):
    name: str
    message: str


@router.get("/")
async def home():
    return {"message": "All running good!", "status": 200}


@router.post("/api/post_test")
async def recieved_msg(msg: Message):
    try:
        return {"Recieved": True, "Message": f"{msg.name} said: {msg.message}"}
    
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/api/test")
async def testing():
    return {"Message": "Hello, I'm running"}
