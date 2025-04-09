from openai import OpenAI
from app.config import settings


async def generate_reply(mail_body: str) -> str:
    client = OpenAI(api_key=settings.OPENROUTER_API_KEY, base_url=settings.BASE_URL_ROUTER_API)

    response = client.chat.completions.create(
            model="deepseek/deepseek-chat:free",   
            messages=[
            {
                "role": "user",
                "content": 
                """
                Write a polite, professional,
                and naturally written email response to the message below.
                Include a greeting and closing. Answer any questions if present,
                and provide helpful or informative details if needed.
                Incoming email: 
                \"\"\"
                {mail_body}
                \"\"\"
                """
            },
        ]
        )
    
    return response.choices[0].message.content.strip()
