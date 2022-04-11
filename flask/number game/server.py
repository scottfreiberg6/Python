from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
import random
app.secret_key="tunnel"

@app.route('/')
def number():
    if "number" not in session:
        session ['number'] = random.randint(1, 100)

        return render_template("index.html")

@app.route('/num1', methods=['post'])
def guess():
    count=0
    if 'num1' in session:
        session['num1']= int(request.form['num1'])
        count+=1
    return redirect ('/')

@app.route ('/reset')
def num_reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True, port=5001)