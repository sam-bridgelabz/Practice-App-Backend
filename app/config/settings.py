import os
from dotenv import load_dotenv
from app.config.logger import AppLogger

logger = AppLogger.get_logger()

load_dotenv()

class BaseConfig:
    ENVIRONMENT = os.getenv("ENV", "DEV")

    DB_USER = os.getenv("DB_USER", "DEV")
    DB_PASS = os.getenv("DB_PASS", "DEV")
    DB_HOST = os.getenv("DB_HOST", "DEV")
    DB_NAME = os.getenv("DB_NAME", "DEV")

    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY", "DEV")
    AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", "DEV")
    AWS_REGION = os.getenv("AWS_REGION", "DEV")
    AWS_BUCKET = os.getenv("AWS_BUCKET", "DEV")

    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_TEMPERATURE = float(os.getenv("GEMINI_TEMPERATURE", 1.0))
    DEBUG = False

class DevConfig(BaseConfig):
    DEBUG = True
    GEMINI_TEMPERATURE = 0.0

class ProdConfig(BaseConfig):
    DEBUG = False
    GEMINI_TEMPERATURE = 0.0

# Pick config based on ENV
settings = DevConfig() if BaseConfig.ENVIRONMENT == "DEV" else ProdConfig()
if settings:
    logger.info("Environment variables initialized")
else:
    logger.error("Environment not found")
    raise ValueError("Environment not found for")
