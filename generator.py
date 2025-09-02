from config import OPENAI_API_KEY
import httpx

async def generate_reply(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    json_data = {
        "model": "gpt5",
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post("https://api.openai.com/v1/chat/completions", json=json_data, headers=headers)

            # Проверка успешного ответа
            if response.status_code == 200:
                data = response.json()
                return data["choices"][0]["message"]["content"]
            else:
                error_details = response.json()
                return f"❌ OpenAI API ошибка {response.status_code}: {error_details.get('error', {}).get('message', 'Неизвестная ошибка')}"

    except Exception as e:
        return f"❌ Ошибка запроса: {e}"
