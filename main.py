from flask import Flask, render_template 

app = Flask("Amor")

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/cartao")
def hello_cartao():
    return render_template("cartao.html")

app.run(host='0.0.0.0')