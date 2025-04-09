from fastapi import FastAPI
from app.schemas import MailInput, MailOutput
from app.openai_service import generate_reply
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "chrome-extension://nbiokjkgehnocmhgkolgkobnheknpfoe",  # Buraya chrome extension ID'ni koyacağız
    "http://localhost:8000",  # localhost'tan gelen isteklere izin ver
    "http://127.0.0.1:8000",  # Yerel API isteği
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # İzin verilen kaynaklar
    allow_credentials=True,
    allow_methods=["*"],  # Tüm HTTP yöntemlerine izin ver
    allow_headers=["*"],  # Tüm başlıklara izin ver
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/generate-reply", response_model=MailOutput)
async def generate_mail_reply(data: MailInput):
    reply = await generate_reply(data.mail_body)
    return {"reply": reply}