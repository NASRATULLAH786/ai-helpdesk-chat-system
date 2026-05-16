from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.database import SessionLocal, ChatHistory


app = FastAPI(title="AI Helpdesk Chat System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "AI Helpdesk Chat System Running"}


@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message.lower()

    if "refund" in user_message:
        reply = "Refunds are processed within 3-5 business days."
    elif "password" in user_message:
        reply = "Use the password reset link on the login page."
    elif "urgent" in user_message:
        reply = "Your issue has been marked as urgent and escalated."
    else:
        reply = "Our support team will assist you shortly."

    db = SessionLocal()

    chat_record = ChatHistory(
        user_message=request.message,
        bot_reply=reply
    )

    db.add(chat_record)
    db.commit()
    db.close()

    return {
        "user_message": request.message,
        "reply": reply
    }


@app.get("/history")
def get_history():
    db = SessionLocal()
    chats = db.query(ChatHistory).all()

    results = []

    for chat in chats:
        results.append({
            "user_message": chat.user_message,
            "bot_reply": chat.bot_reply
        })

    db.close()

    return results