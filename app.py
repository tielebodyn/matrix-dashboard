from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/gif1")
def gif1():
    return render_template('gif1.html')
@app.route("/gif2")
def gif2():
    return render_template('gif2.html')
@app.route("/gif3")
def gif3():
    return render_template('gif3.html')
@app.route("/gif4")
def gif4():
    return render_template('gif4.html')
@app.route("/gif5")
def gif5():
    return render_template('gif5.html')
@app.route("/gif6")
def gif6():
    return render_template('gif6.html')
@app.route("/gif7")
def gif7():
    return render_template('gif7.html')
@app.route("/gif8")
def gif8():
    return render_template('gif8.html')




if __name__ == "__main__":
    app.run()