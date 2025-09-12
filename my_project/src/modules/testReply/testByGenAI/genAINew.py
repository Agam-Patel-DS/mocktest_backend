from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import json, re
import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if groq_api_key:
    print("GROQ_API_KEY loaded successfully!")
else:
    print("GROQ_API_KEY not found. Make sure it's in your .env file.")

# Initialize Groq LLM
llm = ChatGroq(
    temperature=0.2,   # lower temperature = more deterministic
    groq_api_key=groq_api_key,
    model="llama-3.1-8b-instant"
)

# Strict JSON-only prompt
# prompt = ChatPromptTemplate.from_template("""
# You are a DSA coding question generator.

# Generate **EXACTLY {num_questions}** questions on the topics: {topics}.
# Each must be assigned one of these difficulties: {difficulties}.
# ⚠️ Every requested difficulty level MUST appear at least once.
# ⚠️ Generate no more and no less than {num_questions} questions.

# Return the result as VALID JSON ONLY, with this exact structure:

# {{
#   "1": {{
#     "question": "problem_statement",
#     "difficultyLevel": "difficultyLevelofthequestion",
#     "examples": {{
#       "1": {{
#         "input": "some_input",
#         "output": "some_output",
#         "explanation": "some_explanation"
#       }}
#     }},
#     "constraints": {{
#       "1": "someConstraint",
#       "2": "someConstraint"
#     }}
#   }},
#   "2": ...
# }}

# Do not include explanations, notes, or extra text outside JSON.
# """)

prompt = ChatPromptTemplate.from_template("""You are a DSA coding question generator.

Generate EXACTLY {num_questions} questions on the topics: {topics}.
Each must be assigned one of these difficulties: {difficulties}.

⚠️ Every requested difficulty level MUST appear at least once.
⚠️ Generate no more and no less than {num_questions} questions.
⚠️ No two questions should be the same — they must be mutually exclusive in the data structure or algorithm they focus on.
⚠️ Question statements must be longer, descriptive, and real-world inspired, avoiding overly short or generic prompts.

Return the result as VALID JSON ONLY, with this exact structure:

{{
  "1": {{
    "question": "problem_statement",
    "difficultyLevel": "difficultyLevelofthequestion",
    "examples": {{
      "1": {{
        "input": "some_input",
        "output": "some_output",
        "explanation": "some_explanation"
      }}
    }},
    "constraints": {{
      "1": "someConstraint",
      "2": "someConstraint"
    }}
  }},
  "2": ...
}}
"""
)

def safe_json_parse(text: str):
    """Strict JSON extraction & parsing with cleanup."""
    try:
        # Remove junk before/after JSON using regex
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            raise ValueError("No JSON found")
        json_str = match.group(0)
        return json.loads(json_str)
    except Exception as e:
        print("❌ JSON parse failed:", e)
        print("Raw response:", text)
        return None

def generate_questions(num_questions: int, topics: list, difficulties: list, retries=2):
    chain = prompt | llm

    for attempt in range(retries):
        response = chain.invoke({
            "num_questions": num_questions,
            "topics": topics,
            "difficulties": difficulties
        })

        parsed = safe_json_parse(response.content)
        if not parsed:
            continue

        # ✅ Validate count
        if len(parsed) == num_questions:
            return parsed
        else:
            print(f"⚠️ Attempt {attempt+1}: Got {len(parsed)} instead of {num_questions}")

    print("❌ Model failed to generate correct number of questions after retries.")
    return None
