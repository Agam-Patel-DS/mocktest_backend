from flask import Flask, request, jsonify
from src.replies.testReplyFinal import testByCompaniesReplyFinal,testByDifficultyReplyFinal
from src.utils.customException import handle_exceptions
from src.utils.customLogger import logger
from pathlib import Path


app=Flask(__name__)

@handle_exceptions
@app.route("/get_questions_dsa",methods=["POST"])
def get_questions_dsa():
    data=request.get_json()

    logger.info(f"{Path(__file__).name}: new request at /get_questions_dsa")

    if not data:
        logger.info(f"{Path(__file__).name}: No data recieved")
        return jsonify({"error":"No JSON data recieved"}), 400
    
    questionsDict,dbDict=testByDifficultyReplyFinal(data)

    logger.info(f"{Path(__file__).name}: response sent to frontend")

    return jsonify({
        "questionsDict":questionsDict,
        "dbDict":dbDict
    })

@handle_exceptions
@app.route("/get_questions_companies",methods=["POST"])
def get_questions_companies():
    data=request.get_json()

    logger.info(f"{Path(__file__).name}: new request at /get_questions_companies")

    if not data:
        return jsonify({"error":"No JSON data recieved"}), 400
    
    questionsDict,dbDict=testByCompaniesReplyFinal(data)

    logger.info(f"{Path(__file__).name}: response sent to frontend")

    return jsonify({
        "questionsDict":questionsDict,
        "dbDict":dbDict
    })


if __name__=="__main__":
    app.run(debug=True)