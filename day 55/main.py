from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def bold_wrapper():
       return f"<b>{function()}</b>"

    return bold_wrapper

def make_emphasis(function):
    def emphasis_wrapper():
       return f"<em>{function()}</em>"

    return emphasis_wrapper

def make_underlined(function):
    def underlined_wrapper():
       return f"<u>{function()}</u>"

    return underlined_wrapper


@app.route("/")
def hello_world():
    return 'Hello, World!'


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def hello_bye():
    return "Bye!"

if __name__ == '__main__':  
   app.run(debug=True)