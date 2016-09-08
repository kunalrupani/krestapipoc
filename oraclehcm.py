

from flask import Flask, redirect, url_for,request, render_template, Response, jsonify

from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db= client.hcmdb

@app.route('/')
def greetings():

	_items =db.hcmdb.find()
	items = [item for item in _items]

	return render_template('hcmindex.html', items=items)

@app.route('/employees')
def empinfo():
	_items =db.hcmdb.find()
	items = [item for item in _items]
	output = []
	for q in items:
		output.append({'name': q['name'], 'SSN': q['SSN']})
	return jsonify(output)	

@app.route('/addnewemp', methods=['POST'])
def addemp():
	emp_rec = {
		"name" : request.form['name'],
		"address" : request.form['address'],
		"SSN" : request.form['ssn'],
		"Salary": request.form['salary']
	}
	
	#Insert record into MongoDB
	db.hcmdb.insert_one(emp_rec)

    #Return to main page 
	return redirect(url_for('greetings'))

if __name__ == "__main__":
	app.run(debug=True)