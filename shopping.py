from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)

app.secret_key = "secret"

@app.route("/", methods=["GET", "POST"])
def store():
    if request.method == "GET":
        return render_template("store.html")

    if request.method == "POST":
        for item in ["eggs", "milk", "bread"]:
            if item not in session :
                session[item] = int(request.form[item])
            else:
                session[item] += int(request.form[item])
        return redirect(url_for("cart"))
    

@app.route("/cart", methods=["GET", "POST"])
def cart():

    cart = []
    for item in ["eggs", "milk", "bread"]:
        cart.append({"name":item.capitalize(), "quantity":session[item]})
    return render_template("cart.html", cart=cart)


@app.route("/buy", methods=["GET", "POST"])
def buy():

        amount = 0

    index = 0

    prices = [5, 12, 22]

    cart = []
    for item in ["eggs", "milk", "bread"]:
        row = {}
        row["name"] = item.capitalize()
        row["quantity"] = session[item]
        row["price"] = prices[index] * session[item]
        amount = amount + row["price"]
        cart.append(row)
        index = index + 1
    return render_template("bill.html", cart=cart, amount=amount)

if __name__ == '__main__':
	app.run()
