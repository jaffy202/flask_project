from flask import Flask
import random

random_value = random.randint(0, 9)

app = Flask(__name__)


@app.route('/')
def question():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="/static/guess.jpg" width=400 />')


@app.route('/<int:guessed_number>')
def check_answer(guessed_number):
    if guessed_number == random_value:
        return '<h1 style="color:lime">You found me</h1><img src="/static/found_me.jpg" width=400 />'
    elif guessed_number > random_value:
        return '<h1 style="color:red">Too High, try again!</h1><img src="/static/high.jpg" width=400 />'
    else:
        return '<h1 style="color:pink">Too Low, try again!</h1><img src="/static/low.jpg" width=400 />'


if __name__ == '__main__':
    app.run(debug=True)
