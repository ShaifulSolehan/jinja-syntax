from flask import Flask,render_template

app = Flask(__name__,template_folder="templates")
todos=[
    ("Get coffee",True),
    ("Learn programming",False),
    ("Sleep",True)
]
@app.route("/")
def home():
    return render_template("home.html",todos=todos)
