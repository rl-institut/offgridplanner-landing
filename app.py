from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/license")
def license():
    return render_template("license.html")

@app.route("/sponsoring")
def sponsoring():
    return render_template("sponsoring.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/imprint")
def imprint():
    return render_template("imprint.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
