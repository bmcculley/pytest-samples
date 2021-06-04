from flask import Flask, jsonify, request, session

app = Flask(__name__)

app.secret_key = "4bfb977d-8532-48bf-83da-030d2ad3b8ad"
app.balance = 0

@app.route('/v1/deposit/<int:amount>', methods=['PUT'])
def deposit(amount):
	app.balance += amount
	response = jsonify({'deposited':'%.2f'% amount})
	response.status_code = 200
	return response

@app.route('/v1/withdraw/<int:amount>', methods=['PUT'])
def withdraw(amount):
	if app.balance >= amount:
		app.balance -= amount
		response = jsonify({'withdrew':'%.2f'% amount})
	else:
		response = jsonify({'withdrew':'Insufficient balance.'})
	response.status_code = 200
	return response

@app.route('/v1/display', methods=['GET'])
def display():
	response = jsonify({'balance':'%.2f'% app.balance})
	response.status_code = 200
	return response

if __name__ == '__main__':
	app.run(debug=True)