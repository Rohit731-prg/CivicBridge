from fastapi_mail import ConnectionConfig
from app.Config.Config import setting

conf = ConnectionConfig(
    MAIL_USERNAME=setting.MAIL_USERNAME,
    MAIL_PASSWORD=setting.MAIL_PASSWORD,
    MAIL_FROM=setting.MAIL_FROM,
    MAIL_PORT=setting.MAIL_PORT,
    MAIL_SERVER=setting.MAIL_SERVER,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True
)