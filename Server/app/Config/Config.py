from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    DB_URL: str = ""
    SERECT_KEY: str = ""
    CLOUDINARY_NAME: str = ""
    CLOUDINARY_KEY: str = ""
    CLOUDINARY_SECRET: str = ""

    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""
    MAIL_FROM = ""
    MAIL_PORT = 0
    MAIL_SERVER = ""
    MAIL_STARTTLS = None,
    MAIL_SSL_TLS = None,
    USE_CREDENTIALS = None

    class Config:
        env_file = ".env"

setting = Setting()