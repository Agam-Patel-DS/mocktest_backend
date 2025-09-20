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


# Prompt template for correctness checking
prompt = ChatPromptTemplate.from_template("""
You are a DSA evaluator. 
You are given a coding question and its proposed solution.
Your task:
1. Verify if the solution is correct for the question.
2. If correct: return {{"result": true, "testCase": null, "explanation": null}}.
3. If incorrect: return {{"result": false, "testCase": "a failing input case", "explanation": "reason why it fails"}}.

Question (ID: {qid}):
{question}

Proposed Solution:
{solution}

Return only a JSON dictionary as instructed.
""")

def evaluate_solution(qid, question, solution):
    """Evaluate a single solution against its question."""
    chain = prompt | llm
    response = chain.invoke({"qid": qid, "question": question, "solution": solution})
    
    try:
        return json.loads(response.content)
    except:
        return {"result": False, "testCase": None, "explanation": "Invalid JSON response"}

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
