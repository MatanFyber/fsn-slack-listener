from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/getNewMessage', methods=['GET', 'POST'])
def getNewMessage():
	content = request.get_json(force=True)
	
	return jsonify(challenge=content['challenge']), 200
	

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)