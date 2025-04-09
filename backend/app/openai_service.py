from openai import OpenAI
from app.config import settings
import os
from dotenv import load_dotenv

#.env load file
load_dotenv()

async def generate_reply(mail_body: str) -> str:
    client = OpenAI(api_key=settings.OPENROUTER_API_KEY, base_url=settings.BASE_URL_ROUTER_API)
    prompt = os.getenv("prompt")

    response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo-0613",   
            messages=[
            {
                "role": "user",
                "content": f"""{prompt} 
                Incoming email: 
                \"\"\"
                {mail_body}
                \"\"\"
                """
            },
        ]
        )
    
    return response.choices[0].message.content.strip()
