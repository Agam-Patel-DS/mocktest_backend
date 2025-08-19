from flask import Flask, request, jsonify
from src.modules.testReply.testReplyFinal import testReplyFinal
from src.utils.customException import handle_exceptions
app=Flask(__name__)

@handle_exceptions
@app.route("/get_questions",methods=["POST"])
def get_questions():
    data=request.get_json()
    if not data:
        return jsonify({"error":"No JSON data recieved"}), 400
    
    questionsDict,dbDict=testReplyFinal(data)

    return jsonify({
        "questionsDict":questionsDict,
        "dbDict":dbDict
    })


if __name__=="__main__":
    app.run(debug=True)