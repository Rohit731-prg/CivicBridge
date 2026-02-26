from fastapi_mail import FastMail, MessageSchema, MessageType
from pydantic import EmailStr
from app.Config.config_email import conf

async def send_otp_email(email: EmailStr, otp: str):
    message = MessageSchema(
        subject="ClearDay OTP Verification",
        recipients=[email],
        body=f"Your OTP is: {otp}\nIt will expire in 5 minutes.",
        subtype=MessageType.plain
    )

    fm = FastMail(conf)  # FastMail is the class and fm is the object
    await fm.send_message(message)