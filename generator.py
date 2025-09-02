from config import OPENAI_API_KEY
import httpx

async def generate_reply(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    json_data = {
        "model": "gpt-4",
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post("https://api.openai.com/v1/chat/completions", json=json_data, headers=headers)
            return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Ошибка: {e}"
