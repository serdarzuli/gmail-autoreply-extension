from pydantic import BaseModel

class MailInput(BaseModel):
    mail_body: str

class MailOutput(BaseModel):
    reply: str
