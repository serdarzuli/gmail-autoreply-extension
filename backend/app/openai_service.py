from openai import OpenAI
from app.config import settings


async def generate_reply(mail_body: str) -> str:
    client = OpenAI(api_key=settings.OPENROUTER_API_KEY, base_url=settings.BASE_URL_ROUTER_API)

    response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo-0613",   
            messages=[
            {
                "role": "user",
                "content": 
                f"""
                Below is an email received from a customer.
                Provide a professional and polite response that directly addresses the message. 
                Answer any questions clearly and completely. 
                Avoid unnecessary repetition and vague expressions. 
                End the response with a friendly closing that leaves the door open for further communication.

                Incoming email: 
                \"\"\"
                {mail_body}
                \"\"\"
                """
            },
        ]
        )
    
    return response.choices[0].message.content.strip()
