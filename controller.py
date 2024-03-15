from flask import Flask, render_template, request, jsonify
from random import choice
import time

app = Flask(__name__)

arrows = ['up', 'down', 'left', 'right']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game')
def start_game():
    return render_template('game.html')

@app.route('/get_prompt')
def get_prompt():
    prompt = choice(arrows)
    time.sleep(1)  
    return jsonify({'prompt': prompt})

if __name__ == '__main__':
    app.run(debug=True)
