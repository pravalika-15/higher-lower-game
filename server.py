from flask import Flask
import random

app = Flask(__name__)

num = random.randint(0, 10)

@app.route('/')
def guess_number():
    return '<h1>Guess the number: </h1>'


@app.route('/<int:number>')
def check(number):
    if num > number:
        print("Too low!! try again!")
        return '<img src="https://media.giphy.com/media/3oKHWfu68Q6XOz2I6Y/giphy.gif">'
    elif num == number:
        print("Perfect!! Bravo!!")
        return '<img src="https://media.giphy.com/media/YRhUem7n2UaF9EK2PH/giphy.gif">'
    elif num < number:
        print("Too high!! try again!")
        return '<img src="https://media.giphy.com/media/27sdoZn8YhLbil01q6/giphy.gif">'
    else:
        print("check whether u entered an integer")
        return '<img src="https://media.giphy.com/media/fV2nYFD3akDuTUgVhy/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
