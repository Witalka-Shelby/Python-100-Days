from flask import Flask
import random

app = Flask(__name__)
number_to_guess = random.randint(0, 9)

@app.route("/")
def guessing_game():
    return "<h1>Guess a number between 0 and 9 </h1> \
        <img src='https://media.giphy.com/media/CmoAZcsJ33ShWqufbd/giphy.gif'> \
        "


def logic_func(function):
    def wrapper(**kwargs):
        print(number_to_guess)
        print(kwargs)
        if number_to_guess == int(kwargs["number"]):
            return "<h1>You found me!</h1> \
            <img src='https://media.giphy.com/media/3NtY188QaxDdC/giphy.gif'>"
        elif number_to_guess < int(kwargs["number"]):
            return "<h1>Too high, try again!</h1> \
            <img src='https://media.giphy.com/media/Z9hZLKflOlXjo349De/giphy.gif'>"
        else:
            return "<h1>Too low, try again!</h1> \
            <img src='https://media.giphy.com/media/l1KVaj5UcbHwrBMqI/giphy.gif'>"
    
    return wrapper

@app.route("/<number>")
@logic_func
def test(number):
    return f"{number} cheat: {number_to_guess}"

if __name__ == '__main__':
    app.run(debug=True)