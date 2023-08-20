from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculator/greeting', methods=['GET'])
def check_service():
    return "Hello world!", 200

@app.route('/calculator/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    first = data['first']
    second = data['second']
    result = first + second
    response_data = {"result": result}
    return jsonify(response_data), 200

@app.route('/calculator/subtract', methods=['POST'])
def subtract_numbers():
    data = request.get_json()
    first = data['first']
    second = data['second']
    result = first - second
    response_data = {"result": result}
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')