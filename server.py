from flask import Flask, jsonify 
app = Flask(__name__)

@app.route('/', methods=['GET'])
def version():
    return jsonify({'name': 'BACKEND PYTHON', 'version': '0.1.0'})

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8081, debug=True)