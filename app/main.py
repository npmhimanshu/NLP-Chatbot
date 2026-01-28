from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from .chatbot import get_response

app = FastAPI(title="NLP Chatbot API")

templates = Jinja2Templates(directory="app/templates")

class UserMessage(BaseModel):
    message: str

@app.post("/chat/")
def chat(user_message: UserMessage):
    response = get_response(user_message.message)
    return {"response": response}

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
