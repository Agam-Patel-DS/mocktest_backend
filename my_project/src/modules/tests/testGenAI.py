from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
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

# ---------------- Enforcing Schema ----------------
response_schemas = [
    ResponseSchema(name="result", description="True if solution is correct, else False"),
    ResponseSchema(name="testCase", description="The test case if incorrect, otherwise null"),
    ResponseSchema(name="explanation", description="Explanation if incorrect, otherwise null"),
]

parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = parser.get_format_instructions()

# Prompt template for correctness checking
prompt = ChatPromptTemplate.from_template(
    """
You are a DSA evaluator. 
You are given a coding question and its proposed solution.
Your task:
1. Verify if the solution is correct for the question.
2. If correct: return as per the JSON schema.
3. If incorrect: return as per the JSON schema with a failing test case and explanation.

Question (ID: {qid}):
{question}

Proposed Solution:
{solution}

Return only a JSON object in this exact format:
{format_instructions}
""",
    partial_variables={"format_instructions": format_instructions}
)

def extract_json(text: str):
    """Try to extract a JSON object from raw text."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except Exception:
            return None
    return None

def evaluate_solution(qid, question, solution):
    """Evaluate a single solution against its question."""
    chain = prompt | llm
    response = chain.invoke({"qid": qid, "question": question, "solution": solution})
    
    # First attempt: strict parser
    try:
        return parser.parse(response.content)
    except Exception as e:
        # Second attempt: regex salvage
        parsed = extract_json(response.content)
        if parsed:
            return parsed
        # Final fallback: structured error
        return {"result": False, "testCase": None, "explanation": f"Invalid JSON response: {str(e)}"}

def evaluate_all(questions_dict, solutions_dict):
    """Evaluate all solutions and return final dictionary."""
    results = {}
    print(f"evaluate_all func called for \n questions: {questions_dict}\n solutions: {solutions_dict}")
    for qid, question in questions_dict.items():
        print(f"qid: {qid}\n question: {question}")
        sol = solutions_dict.get(qid)
        if sol is None:
            try:
                sol = solutions_dict.get(int(qid))
            except ValueError:
                pass
        print(f"sol:{sol}")
        if sol is None:
            results[qid] = {"result": False, "testCase": None, "explanation": "No solution provided"}
            print(results[qid])
        else:
            results[qid] = evaluate_solution(qid, question, sol)
            print(results[qid])
    return results

def count_correct_solutions(results_dict):
    """Count how many solutions are correct in the results dict."""
    return sum(1 for res in results_dict.values() if res["result"] is True)


# # ---------------- Example ----------------
# questions = {
#     "q1": "Given an array, find the maximum subarray sum using Kadane's Algorithm.",
#     "q2": "Check if a string is palindrome."
# }

# solutions = {
#     "q1": "def maxSubArray(nums): return max(nums)",  # wrong
#     "q2": "def isPalindrome(s): return s == s[::-1]"  # correct
# }

# final_results = evaluate_all(questions, solutions)
# print(final_results)   # dictionary output

# correct_count = count_correct_solutions(final_results)
# print("Correct Solutions:", correct_count)
