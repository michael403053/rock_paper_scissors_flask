from flask import render_template
from app import app
from models.rps import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<player1_choice>/<player2_choice>')
def return_winner(player1_choice, player2_choice):
    result = win_finder(player1_choice, player2_choice)
    return render_template('result.html', result=result, player1_choice=player1_choice, player2_choice=player2_choice)