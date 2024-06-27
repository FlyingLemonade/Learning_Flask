"""
HTML folder names need to be
'templates'

Tempalte inheritance works by,
extending the parent(s) html to the childs html,
then in childs html we need to define the "blocks"
section in that defined in the parent html.

example of block : 
in parent
{% block content %} {% endblock %}

in child
{% block content %} Title {% endblock %}

Simply, define the content that we want to apply
in every child html outside {% block %}{% endblock %}

"""

from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)
# app.config['DEBUG'] = True
@app.route("/")
def home():
    return render_template("index.html", content="Hai!")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/admin")
def admin():
    return redirect(url_for("user",name="admin")) #url_for(name of the function, parameter if any)

if __name__ == "__main__":
    app.run(debug=True)



