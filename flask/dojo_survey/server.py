from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "tunnell"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=["post"])
def process():
    print(request.form)
    print(request.form["name"])
    print(request.form["location"])
    print(request.form["favorite_language"])
    print("this is a processing route")

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['favorite_language']
    session['comments'] = request.form['comments']

    return redirect("/result")


@app.route("/result")


def show_info():
    print(session["name"])
    return render_template("result.html", name=session["name"], location=session["location"], language=session["language"], comments=session["comments"])


if __name__ == "__main__":
    app.run(debug=True, port=5002)
