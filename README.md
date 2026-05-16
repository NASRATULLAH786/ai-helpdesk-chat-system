<<<<<<< HEAD
# AI Helpdesk Chat System

A full-stack AI-powered helpdesk chat application built using FastAPI, JavaScript, SQLite, and automation-driven conversational workflows.

The system allows users to:
- send support messages
- receive automated AI-style responses
- store chat history in SQLite
- reload previous conversations
- simulate intelligent customer support workflows

---

# Screenshots

## Chat Interface

![Chat UI](screenshots/chat-ui.png)

## API Documentation

![Swagger API](screenshots/swagger-api.png)

---

# Features

## AI Helpdesk Workflow
Supports automated responses for:
- password reset issues
- refund requests
- urgent support escalation
- general customer support

## Backend API
Built using FastAPI REST endpoints.

## SQLite Chat History
Stores:
- user messages
- AI replies
- persistent conversation history

## Frontend Chat Interface
Interactive web-based support chat dashboard.

## Automation Logic
Demonstrates:
- workflow automation
- conversational processing
- support ticket simulation

---

# Tech Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy
- JavaScript
- HTML/CSS
- REST APIs

---

# Project Structure

```bash
ai-helpdesk-chat-system/
│
├── app/
│   ├── main.py
│   └── database.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── screenshots/
│   ├── chat-ui.png
│   └── swagger-api.png
│
├── requirements.txt
└── README.md
```

---

# API Endpoints

## Send Chat Message

```http
POST /chat
```

### Example Request

```json
{
  "message": "I forgot my password"
}
```

---

## Load Chat History

```http
GET /history
```

Returns saved conversations from SQLite database.

---

# Setup Instructions

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-helpdesk-chat-system.git
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Backend

```bash
uvicorn app.main:app --reload --port 8081
```

## Open Frontend

Open:

```text
frontend/index.html
```

in your browser.

---

# Future Improvements

- Real LLM integration
- Authentication system
- Multi-user chat
- Ticket management
- Admin dashboard
- Cloud deployment
- Docker support
- Email notifications

---

# Author

Nasratullah Mirzai
=======
# ai-helpdesk-chat-system
>>>>>>> 44186905cf6b9bb1f1e83142e42304333e0b913e
