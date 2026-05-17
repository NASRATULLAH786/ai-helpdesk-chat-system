from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

from app.database import SessionLocal, ChatHistory

app = FastAPI(
    title="AI Helpdesk Chat System",
    description="AI-powered customer support automation and workflow management platform."
)

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
    return {
        "message": "AI Helpdesk Chat System Running",
        "status": "active",
        "timestamp": datetime.utcnow()
    }


@app.post("/chat")
def chat(request: ChatRequest):

    user_message = request.message.lower()

    category = "general"
    priority = "normal"

    if "refund" in user_message:
        category = "billing"
        reply = (
            "Your refund request has been submitted successfully. "
            "Refunds are typically processed within 3-5 business days."
        )

    elif "password" in user_message:
        category = "authentication"
        reply = (
            "Please use the password reset option available on the login page. "
            "A reset link will be sent to your registered email address."
        )

    elif "urgent" in user_message:
        category = "escalation"
        priority = "high"

        reply = (
            "Your request has been marked as urgent and escalated "
            "to the support team for immediate review."
        )

    elif "payment" in user_message:
        category = "payment"

        reply = (
            "We detected a payment-related issue. "
            "Please verify your payment details or contact billing support."
        )

    else:
        reply = (
            "Thank you for contacting AI Support. "
            "Our support workflow system has received your request."
        )

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
        "reply": reply,
        "category": category,
        "priority": priority,
        "status": "processed"
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

    return {
        "total_conversations": len(results),
        "history": results
    }