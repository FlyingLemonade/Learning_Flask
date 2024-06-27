from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>hello world!</h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("user",name="admin")) #url_for(name of the function, parameter if any)

if __name__ == "__main__":
    app.run()



