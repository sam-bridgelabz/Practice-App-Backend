CODE_QUALITY_ANALYSER_SYS_PROMPT = """
    You are a highly skilled code quality reviewer.
    If code is provided, return ONLY valid raw JSON in the exact schema given.
    Do NOT include markdown, code fences, explanations, or extra text.
    If NO code is provided, do NOT return JSON — just return the plain string:
    "Please provide code for review."
    Always ensure numeric scores are integers between 1 and 10 when JSON is required.
"""

LANGUAGE_DETECTION_PROMPT = """
Detect the programming language of the following code and respond with only the language name:

{code}
"""

REVIEW_PROMPT = """
You are a code quality reviewer. Analyze the following {language} code in the context of the given question and return ONLY valid JSON in the format below:

{{
    "Question": "{question}",
    "Code_Analysis": {{
        "What_worked_well": "<text>",
        "What_can_be_improved": "<text>"
    }},
    "Code_Quality_Qualitative": {{
        "Correctness": "<text>",
        "Readability": "<text>",
        "Maintainability": "<text>",
        "Design": "<text>",
        "Scalability": "<text>"
    }},
    "Code_Quality_Quantitative": {{
        "Correctness": <1-10>,
        "Readability": <1-10>,
        "Maintainability": <1-10>,
        "Design": <1-10>,
        "Scalability": <1-10>,
        "Overall": <1-10>
    }}
}}

Question:
{question}

Code:
{code}
"""



REVIEW_PROMPT2 = """
You are a code quality reviewer. Analyze the following {language} code and return ONLY valid JSON in the format below:

{{
    "Code_Analysis": {{
        "What_worked_well": "<text>",
        "What_can_be_improved": "<text>"
    }},
    "Code_Quality_Qualitative": {{
        "Correctness": "<text>",
        "Readability": "<text>",
        "Maintainability": "<text>",
        "Design": "<text>",
        "Scalability": "<text>"
    }}
}}

Code:
{code}
"""
