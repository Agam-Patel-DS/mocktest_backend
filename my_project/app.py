from flask import Flask, request, jsonify
from src.replies.testReplyFinal import testByCompaniesReplyFinal,testByDifficultyReplyFinal
from src.utils.customException import handle_exceptions
app=Flask(__name__)

@handle_exceptions
@app.route("/get_questions_dsa",methods=["POST"])
def get_questions_dsa():
    data=request.get_json()
    if not data:
        return jsonify({"error":"No JSON data recieved"}), 400
    
    questionsDict,dbDict=testByDifficultyReplyFinal(data)

    return jsonify({
        "questionsDict":questionsDict,
        "dbDict":dbDict
    })

@handle_exceptions
@app.route("/get_questions_companies",methods=["POST"])
def get_questions_companies():
    data=request.get_json()
    if not data:
        return jsonify({"error":"No JSON data recieved"}), 400
    
    questionsDict,dbDict=testByCompaniesReplyFinal(data)

    return jsonify({
        "questionsDict":questionsDict,
        "dbDict":dbDict
    })


if __name__=="__main__":
    app.run(debug=True)