from flask import Flask
app = Flask('__name__') 

@app.route("/home")
def hello():
	return "hello welcome to homepage bvcec hello this is vinay sri ram "
