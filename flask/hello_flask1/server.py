from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def hello_dojo():
    return 'Dojo'

@app.route('/say/<name>')          # The "@" decorator associates this route with the function immediately following
def hello_(name):
    return "Hi," + name

@app.route('/repeat/<string:name>/<int:num>')          # The "@" decorator associates this route with the function immediately following
def say_num(name, num):
    return f"hi, {name * num}"




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5001)    # Run the app in debug mode.

