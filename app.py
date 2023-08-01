from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_internet():
    return "Hello Internet!"

@app.route('/name/<name>')
def hello_name(name):
    return 'Hello {}!'.format(name)

@app.route('/get-route', methods=['GET'])
def get_route():
    return 'This is a GET route'

@app.route('/post-route', methods=['POST'])
def post_route():
    return 'This is a POST route'

@app.route('/put-route', methods=['PUT'])
def put_route():
    return 'This is a PUT route'

@app.route('/delete-route', methods=['DELETE'])
def delete_route():
    return 'This is a DELETE route'

@app.route('/route', methods=['GET', 'POST', 'PUT', 'DELETE'])
def my_route():
    if request.method == 'GET':
        return 'This is a GET request'
    elif request.method == 'POST':
        return 'This is a POST request'
    elif request.method == 'PUT':
        return 'This is a PUT request'
    elif request.method == 'DELETE':
        return 'This is a DELETE request'



if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
