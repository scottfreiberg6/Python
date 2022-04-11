from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)

app.secret_key="tunnel"

@app.route('/')
def number():
    if "number" not in session:
        session ['number'] = random.randint(1, 100)

    return render_template("index.html")
    
@app.route('/num1', methods=['POST'])
def guess():
    # count=0
    # if 'number' in session:
    #     session['number']= int(request.form['number'])
    #     count+=1
   
    session['guess']= int (request.form['guess']) 
    return redirect ('/')
    
@app.route('/reset')
def num_reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True, port=5001)