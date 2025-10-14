from app.config.logger import AppLogger
import re
# from app.config.agent_initialization import gemini_agent as code_analyser_agent
from fastapi.responses import JSONResponse
from google.api_core import exceptions as google_exceptions
# from app.utils.github_utils import fetch_github_code
from app.templates.prompts import REVIEW_PROMPT, REVIEW_PROMPT_THEORY
from app.schemas.model_resp_schema import *
import json
from pydantic_ai.settings import ModelSettings
from pydantic_ai.agent import Agent
from app.config.settings import settings
from app.config.agent_initialization import gemini_model
from app.crud.pricing_queries import insert_pricing_data

logger = AppLogger.get_logger()

def generate_model_response(review_results):
    return CodeReviewOutput(
        analysis_output=AnalysisOutput(
            what_worked_well=review_results["Code_Analysis"]["What_worked_well"],
            what_can_be_improved=review_results["Code_Analysis"]["What_can_be_improved"],
        ),
        quality_feedback=QualityFeedback(
            correctness=review_results["Code_Quality_Qualitative"]["Correctness"],
            readability=review_results["Code_Quality_Qualitative"]["Readability"],
            maintainability=review_results["Code_Quality_Qualitative"]["Maintainability"],
            design=review_results["Code_Quality_Qualitative"]["Design"],
            scalability=review_results["Code_Quality_Qualitative"]["Scalability"],
        ),
        quality_scores=QualityScores(
            correctness=review_results["Code_Quality_Quantitative"]["Correctness"],
            readability=review_results["Code_Quality_Quantitative"]["Readability"],
            maintainability=review_results["Code_Quality_Quantitative"]["Maintainability"],
            design=review_results["Code_Quality_Quantitative"]["Design"],
            scalability=review_results["Code_Quality_Quantitative"]["Scalability"],
            overall=review_results["Code_Quality_Quantitative"]["Overall"],
        )
    )

def model_json_error(error_message: str):
    return JSONResponse(
    status_code=500,
    content={"success_status": False, "error_details": str(error_message), "results": None},
    )

def extract_json_from_model_output(text: str) -> str:
    """
    Removes markdown code fences (```json ... ```).
    Returns cleaned JSON string.
    """
    # Remove leading/trailing whitespace and code fences
    cleaned = re.sub(r"^```(?:json)?\n|\n```$", "", text.strip(), flags=re.MULTILINE)
    return cleaned.strip()

# def get_or_extract_code(request):
#     try:
#         # Step 1: Get code based on type
#         if request.type == "github":
#             try:
#                 _, code = fetch_github_code(request.content)
#                 return code
#             except Exception as e:
#                 return json_error(f"Error fetching GitHub code: {str(e)}")
#         elif request.type == "text":
#             return request.content
#         else:
#             return json_error("Invalid type. Must be 'github' or 'text'.")
#     except Exception as e:
#         logger.error(f"Unexpected error fetching code: {str(e)}")

# async def detect_language_with_gemini(code: str) -> str:
#     try:
#         prompt = LANGUAGE_DETECTION_PROMPT.format(code=code)
#         response = await code_analyser_agent.run(prompt)
#         logger.info(f"Detected language: {response}")
#         return response.text.strip()
#     except Exception as e:
#         logger.error(f"Error detecting language: {str(e)}")
#         raise ValueError(f"Error detecting language: {str(e)}")

# async def review_code_with_gemini(question: str, code: str, language: str) -> dict:
#     logger.info(f"Reviewing code for language review_code_with_gemini: {language}")
#     try:

#         prompt = REVIEW_PROMPT.format(language=language, question=question, code=code)

#         code_analyser_agent = Agent(
#         model = gemini_model,
#         system_prompt = CODE_QUALITY_ANALYSER_SYS_PROMPT,
#         model_settings = ModelSettings(
#             temperature=settings.GEMINI_TEMPERATURE,
#             )
#         )

#         if not code_analyser_agent:
#             raise ValueError("Gemini agent not initialized")
#         else:
#             logger.info("Gemini agent initialized")

#             response = await code_analyser_agent.run(prompt)
#             logger.info(f"Code Analysis generated{response.output}")
#             text_output = extract_json_from_model_output(response.output)

#             try:
#                 parsed = json.loads(text_output)
#             except json.JSONDecodeError:
#                 logger.error(f"Agent did not return valid JSON.\nOutput was:\n{text_output}")
#                 raise ValueError(f"Agent did not return valid JSON.\nOutput was:\n{text_output}")
#             return parsed

#     except google_exceptions.GoogleAPICallError as e:
#         logger.error(f"Gemini API error while reviewing code: {str(e)}")
#         raise ValueError(f"Gemini API error while reviewing code: {str(e)}")
#     except Exception as e:
#         logger.error(f"Unexpected error reviewing code: {str(e)}")
#         raise ValueError(f"Unexpected error reviewing code: {str(e)}")

async def review_code_with_gemini(db, user_id: str, prompt_str: str, question: str, code: str, language: str) -> dict:
    logger.info(f"Reviewing code for language review_code_with_gemini: {language}")
    try:
        # if question_type == "TEXT":
        #     prompt = REVIEW_PROMPT_THEORY.format(language=language, question=prompt, code=code)
        # else:
        #     prompt = REVIEW_PROMPT.format(language=language, question=prompt, code=code)

        prompt = prompt_str.format(language=language, question=question, code=code)

        code_analyser_agent = Agent(
            model = gemini_model,
            system_prompt = prompt,
            model_settings = ModelSettings(
                temperature=settings.GEMINI_TEMPERATURE,
                )
        )

        if not code_analyser_agent:
            raise ValueError("Gemini agent not initialized")
        else:
            logger.info("Gemini agent initialized")

            response = await code_analyser_agent.run(prompt)
            logger.info(f"response = {response}")
            # logger.info(f"Code Analysis generated{response.output}")

            insert_pricing_data(db, user_id, "Java", prompt, response)
            text_output = extract_json_from_model_output(response.output)

            try:
                parsed = json.loads(text_output)
            except json.JSONDecodeError:
                logger.error(f"Agent did not return valid JSON.\nOutput was:\n{text_output}")
                raise ValueError(f"Agent did not return valid JSON.\nOutput was:\n{text_output}")
            return parsed

    except google_exceptions.GoogleAPICallError as e:
        logger.error(f"Gemini API error while reviewing code: {str(e)}")
        raise ValueError(f"Gemini API error while reviewing code: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error reviewing code: {str(e)}")
        raise ValueError(f"Unexpected error reviewing code: {str(e)}")
