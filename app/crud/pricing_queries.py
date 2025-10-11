from app.models.pricing_model import GeminiUsage
from app.config.logger import AppLogger

logger = AppLogger.get_logger()



def insert_pricing_data(db, user_id, language, response):
    tokens_input = response.usage.get('prompt_tokens', 0)
    tokens_output = response.usage.get('completion_tokens', 0)

    # Flash-Lite pricing
    COST_PER_INPUT_TOKEN = 0.10 / 1_000_000   # $0.10 per million input tokens
    COST_PER_OUTPUT_TOKEN = 0.40 / 1_000_000  # $0.40 per million output tokens

    cost_input = tokens_input * COST_PER_INPUT_TOKEN
    cost_output = tokens_output * COST_PER_OUTPUT_TOKEN
    total_cost = cost_input + cost_output

    # Log usage in DB
    usage_entry = GeminiUsage(
        user_id=user_id,
        language=language,
        tokens_used=tokens_input + tokens_output,
        cost=total_cost
    )
    db.add(usage_entry)
    db.commit()

    logger.info(f"Logged Gemini usage: {usage_entry}")
