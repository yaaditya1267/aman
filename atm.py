from flask import Flask, redirect, render_template, request, url_for, session
import time
import re

app = Flask(__name__)

app.secret_key = "secret"

@app.route("/", methods=['GET', 'POST'])
def index():
	
	try:
		balance = session["balance"]
		count = session["count"]
	except KeyError:
		count = session["count"] = 0
		balance = session["balance"] = 8000


	if request.method == "GET":
		return render_template("index.html", balance=balance, msg="")

	if request.method == "POST":

		if request.form["amount"] == "" :
			msg = "Amount is required"
			return render_template("index.html", balance=balance, msg=msg)

		if int(request.form["amount"]) < 0 :
			msg = "Cannot enter negative amount"
			return render_template("index.html", balance=balance, msg=msg)

		if session["count"] == 5:
			msg = "5 transactions complete"
			return render_template("index.html", balance=balance, msg=msg)

			if request.form["action"] == 'Withdraw':

			if int(request.form["amount"]) > session["balance"] :
				msg = "Cannot withdraw amount greater than balance"
				return render_template("index.html", balance=balance, msg=msg)

			elif int(request.form["amount"]) > 5000 :
				msg = "Cannot withdraw amount greater than 5000"
				return render_template("index.html", balance=balance, msg=msg)

			else:
				balance = balance - int(request.form["amount"])
				session["balance"] = balance
				session["count"] = session["count"] + 1
				msg = "Money Withdrawn"
				return render_template("index.html", balance=balance, msg=msg)

		elif request.form["action"] == 'Deposit':

			if int(request.form["amount"]) > 10000 :
				msg = "Cannot deposit amount greater than 10000"
				return render_template("index.html", balance=balance, msg=msg)

				else:
				balance = balance + int(request.form["amount"])
				session["balance"] = balance
				session["count"] = session["count"] + 1
				msg = "Money Deposited"
				return render_template("index.html", balance=balance, msg=msg)

if __name__ == '__main__':
	app.run()
