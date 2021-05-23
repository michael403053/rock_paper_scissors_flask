from flask import render_template, redirect, request
from app import app
from models.rps import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<player1_choice>/<player2_choice>')
def return_winner(player1_choice, player2_choice):
    result = win_finder(player1_choice, player2_choice)
    return render_template('result.html', result=result, player1_choice=player1_choice, player2_choice=player2_choice)
    
@app.route('/play')
def play_page():
    return render_template('play.html')

@app.route('/play', methods=['POST'])
def play():
    player_choice = request.form['player_choice']
    player_name = request.form['player_name']
    result = play_rps(player_choice)
    computer_choice = result[1]
    winner = result[0]
    return render_template("play.html", result=result, computer_choice=computer_choice, winner=winner, player_name=player_name)

@app.route('/play/easy')
def play_easy_page():
    return render_template('easy.html')

@app.route('/play/easy', methods=['POST'])
def play_easy():
    player_choice = request.form['player_choice']
    result = play_rps_easy(player_choice)
    player_name = request.form['player_name']
    computer_choice = result[1]
    winner = result[0]
    return render_template("easy.html", result=result, computer_choice=computer_choice, winner=winner, player_name=player_name)

@app.route('/play/hard')
def play_hard_page():
    return render_template('hard.html')

@app.route('/play/hard', methods=['POST'])
def play_hard():
    player_choice = request.form['player_choice']
    result = play_rps_hard(player_choice)
    player_name = request.form['player_name']
    computer_choice = result[1]
    winner = result [0]
    return render_template("hard.html", result=result, computer_choice=computer_choice, winner=winner, player_name=player_name)
    




