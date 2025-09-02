from fastapi import FastAPI
from pydantic import BaseModel
from generator import generate_reply

app = FastAPI()

class Prompt(BaseModel):
    text: str

@app.post("/generate")
async def generate(prompt: Prompt):
    reply = await generate_reply(prompt.text)
    return {"reply": reply}
