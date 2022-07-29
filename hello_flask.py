from flask import Flask, render_template

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template("hello.html")

app.run(host='0.0.0.0', port=24, use_reloader=True)