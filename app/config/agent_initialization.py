from app.config.logger import AppLogger
from app.config.settings import settings
from app.templates.prompts import CODE_QUALITY_ANALYSER_SYS_PROMPT
from pydantic_ai.providers.google_gla import GoogleGLAProvider
from pydantic_ai.models.gemini import GeminiModel
# from pydantic_ai.settings import ModelSettings
# from pydantic_ai.agent import Agent

logger = AppLogger.get_logger()

# ---------Pydantic Codeanalyser Agent ---------
provider = GoogleGLAProvider(api_key=settings.GEMINI_API_KEY)
gemini_model = GeminiModel(
    settings.GEMINI_MODEL,
    provider = provider
    )

# gemini_agent = Agent(
#     model = gemini_model,
#     system_prompt = CODE_QUALITY_ANALYSER_SYS_PROMPT,
#     model_settings = ModelSettings(
#         temperature=settings.GEMINI_TEMPERATURE,
#         )
#     )

# if not gemini_agent:
#     raise ValueError("Gemini agent not initialized")
# else:
#     logger.info("Gemini agent initialized")
