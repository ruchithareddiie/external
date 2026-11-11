from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def home():
	return """
	<html>
	<head>
	    <title> Home page </title>
	</head>
	<body>
	    <h2>home page entered</h2>
	    <p> click below to go ti registration page</p>
	    <a href="/register"> go to registration form </a>
	</body>
	</html
	"""

@app.route("/register")
def register():
	return render_template("register.html") 

@app.route("/success",methods=["POST"])
def success():	
	name=request.form["name"]
	email=request.form["email"]
	phone=request.form["phone"]
	event=request.form["event"]
	return render_template("success.html",name=name,email=email,phone=phone,event=event)

if(__name__ == "__main__"):
	app.run(port=5007, debug=True)