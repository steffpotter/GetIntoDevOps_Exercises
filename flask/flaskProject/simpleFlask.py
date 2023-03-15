# app.py is the main file responsible for running the app
from flask import Flask, Response, request, url_for

# instantiate the Flask application object
app = Flask(__name__)


# decorator-wrapping up function with other function
# set up a route and bind a function as its response
@app.route('/')
def hello_from_flask():
    return "Hello from FLASK"


@app.route('/bye')
def goodbye_from_flask():
    return "Goodbye from FLASK"


@app.route('/get/text')
def get_text():
    return Response("Hello from FLASK using a RESPONSE object")


# http post requests only
@app.route('/post/text', methods=['POST'])
def post_text():
    data_sent = request.data.decode('utf-8')
    return Response("You posted this data to the FLASK app:" + data_sent)


@app.route('/dynamic/<word>')
def say_word(word):
    return word


@app.route('/square/<int:number>')
def square(number):
    squared = number ** 2
    line = "Your number squared is " + str(squared)
    return line


@app.route('/name/<name>')
def greeting(name):
    answer = "Hello " + name + '!!!!!'
    return answer


@app.route('/hello/<names>')
def say_hello_page(name):
    return """
    <html>
         <head>
             <title>Flask App</title>
         </head>
         <body>
            <h1>Name Page</h1>
            <p>Hello {}! </p>
         </body>
    </html>
    """.format(name)


@app.route('/hello/<name>/<int:age>')
def say_hello_name_and_age_page(name, age):
    return """
    <html>
         <head>
             <title>Flask App</title>
         </head>
         <body>
            <h1>Name & Age Page</h1>
            <p>Hello {}! </p>
            <p>You are {} years old. </p>
         </body>
    </html>
    """.format(name, age)


@app.route('/hellowithurl/<name>/<int:age>')
def say_hello_name_and_age_page_url(name, age):
    home_page_endpoint = url_for('hello_from_flask')
    return """
    <html>
         <head>
             <title>Flask App</title>
         </head>
         <body>
            <h1>Name & Age Page</h1>
            <p>Hello {}! </p>
            <p>You are {} years old. </p>
            <hr />
            <a href="{}">Home</a>
         </body>
    </html>
    """.format(name, age, home_page_endpoint)


@app.route('/about')
def about_page():
    steff_endpoint = url_for('greeting', name="Steff")
    saynab_endpoint = url_for('greeting', name="Saynab")
    return """
    <html>
         <head>
             <title>Flask App</title>
         </head>
         <body>
            <h1>About Page</h1>
            <a href="{}">Say hello to Steff</a><br />
            <a href="{}">Say hello to Saynab</a>
         </body>
    </html>
    """.format(steff_endpoint, saynab_endpoint)


# if this script is invoked directly (rather than being imported), run the flask app
if __name__ == "__main__":
    app.run(debug=True)

