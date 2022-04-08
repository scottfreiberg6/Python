from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = "tunnel"

@app.route('/')
def clicker():
    if 'clicker' in session:
        print('clciker exists')
    else:print ("key 'clciker'does not exist")
    
    if "count" in session:
        session["count"] += 1
    else:
        session["count"] = 0
    return render_template("index.html", count= session["count"])

@app.route("/reset")
def reset_session():
    session.clear()
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True, port=5001)