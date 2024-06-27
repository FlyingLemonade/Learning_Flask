from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>hello world!</h1>"

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST" :
        return redirect(url_for("user",usr=request.form["nm"]))
    
    else :
        return render_template("index.html")
@app.route("/<usr>")
def user(usr):
    return f"<h1> Hellow {usr} </h1>"


if __name__ == "__main__":
    app.run(debug=True)



