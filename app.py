import os
import openlit
from fastapi import FastAPI
from pydantic import BaseModel
from google import genai

# ==============================
# Init OpenLIT
# ==============================
openlit.init()

# ==============================
# Gemini Client
# ==============================
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ==============================
# FastAPI App
# ==============================
app = FastAPI()

class ChatRequest(BaseModel):
    message: str

# ==============================
# Model Router
# ==============================
def route_query(message: str) -> str:
    words = len(message.split())
    if words < 20:
        return "gemini-2.0-flash-lite"
    elif words < 100:
        return "gemini-2.0-flash"
    else:
        return "gemini-2.0-pro-exp-02-05"

# ==============================
# Model Caller
# ==============================
def call_model(model_id: str, message: str) -> str:
    try:
        response = client.models.generate_content(
            model=model_id,
            contents=message
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# ==============================
# API Endpoint
# ==============================
@app.post("/chat")
def chat(req: ChatRequest):
    model = route_query(req.message)
    answer = call_model(model, req.message)

    return {
        "model": model,
        "response": answer
    }