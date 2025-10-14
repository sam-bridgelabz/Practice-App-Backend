from app.config.logger import AppLogger
from app.models.pricing_model import GeminiUsage

logger = AppLogger.get_logger()

def insert_pricing_data(db, user_id, language, prompt, response):
    def estimate_tokens(text: str) -> int:
        if not text:
            return 0
        return max(1, len(text) // 4)

    prompt_tokens = estimate_tokens(prompt)
    output_tokens = estimate_tokens(response.output)
    total_tokens = prompt_tokens + output_tokens

    COST_PER_INPUT_TOKEN = 0.10 / 1_000_000
    COST_PER_OUTPUT_TOKEN = 0.40 / 1_000_000

    total_cost = prompt_tokens * COST_PER_INPUT_TOKEN + output_tokens * COST_PER_OUTPUT_TOKEN

    usage_entry = GeminiUsage(
        user_id=user_id,
        language=language,
        tokens_used=total_tokens,
        cost=total_cost
    )
    db.add(usage_entry)
    db.commit()

    logger.info(f"Logged Gemini usage: {usage_entry}")
