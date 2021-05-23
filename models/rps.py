def win_finder(player1_choice, player2_choice):
    p1win = "Player 1 is the winner!"
    p2win = "Player 2 is the winner!"
    tie = "Tie Match!"
    if player1_choice == "rock" and player2_choice  == "paper":
        return p2win
    if player1_choice == "rock" and player2_choice == "scissors":
        return p1win
    if player1_choice == "rock" and player2_choice == "rock":
        return tie
    if player1_choice == "paper" and player2_choice == "paper":
        return tie
    if player1_choice == "paper" and player2_choice == "scissors":
        return p2win
    if player1_choice == "paper" and player2_choice == "rock":
        return p1win
    if player1_choice == "scissors" and player2_choice == "paper":
        return p1win
    if player1_choice == "scissors" and player2_choice == "scissors":
        return tie
    if player1_choice == "scissors" and player2_choice == "rock":
        return p2win

import random

def play_rps(player_choice):
    pwin = "You are the winner!"
    cwin = "Computer is the winner!"
    tie = "Tie Match!"
    rps_list = ["rock", "paper", "scissors"]
    computer_choice = random.choice(rps_list)

    if player_choice == "rock" and computer_choice  == "paper":
        return str(cwin), str(computer_choice)
    if player_choice == "rock" and computer_choice == "scissors":
        return str(pwin), str(computer_choice)
    if player_choice == "rock" and computer_choice == "rock":
        return tie, str(computer_choice)
    if player_choice == "paper" and computer_choice == "paper":
        return tie, str(computer_choice)
    if player_choice == "paper" and computer_choice == "scissors":
        return str(cwin), str(computer_choice)
    if player_choice == "paper" and computer_choice == "rock":
        return str(pwin), str(computer_choice)
    if player_choice == "scissors" and computer_choice == "paper":
        return str(pwin), str(computer_choice)
    if player_choice == "scissors" and computer_choice == "scissors":
        return tie, str(computer_choice)
    if player_choice == "scissors" and computer_choice == "rock":
        return str(cwin), str(computer_choice)

def play_rps_easy(player_choice):
    pwin = "You are the winner!"
    cwin = "Computer is the winner!"
    tie = "Tie Match!"

    if player_choice == "rock":
        computer_choice = random.choice(["rock", "paper", "scissors", "scissors"])

    if player_choice == "paper":
        computer_choice = random.choice(["rock", "paper", "scissors", "rock"])

    if player_choice == "scissors":
        computer_choice = random.choice(["rock", "paper", "scissors", "paper"])
 

    if player_choice == "rock" and computer_choice  == "paper":
        return str(cwin), str(computer_choice)
    if player_choice == "rock" and computer_choice == "scissors":
        return str(pwin), str(computer_choice)
    if player_choice == "rock" and computer_choice == "rock":
        return tie, str(computer_choice)
    if player_choice == "paper" and computer_choice == "paper":
        return tie, str(computer_choice)
    if player_choice == "paper" and computer_choice == "scissors":
        return str(cwin), str(computer_choice)
    if player_choice == "paper" and computer_choice == "rock":
        return str(pwin), str(computer_choice)
    if player_choice == "scissors" and computer_choice == "paper":
        return str(pwin), str(computer_choice)
    if player_choice == "scissors" and computer_choice == "scissors":
        return tie, str(computer_choice)
    if player_choice == "scissors" and computer_choice == "rock":
        return str(cwin), str(computer_choice)

def play_rps_hard(player_choice):
    pwin = "You are the winner!"
    cwin = "Computer is the winner!"
    tie = "Tie Match!"

    if player_choice == "rock":
        computer_choice = random.choice(["rock", "paper", "scissors", "paper"])

    if player_choice == "paper":
        computer_choice = random.choice(["rock", "paper", "scissors", "scissors"])

    if player_choice == "scissors":
        computer_choice = random.choice(["rock", "paper", "scissors", "rock"])
 

    if player_choice == "rock" and computer_choice  == "paper":
        return str(cwin), str(computer_choice)
    if player_choice == "rock" and computer_choice == "scissors":
        return str(pwin), str(computer_choice)
    if player_choice == "rock" and computer_choice == "rock":
        return tie, str(computer_choice)
    if player_choice == "paper" and computer_choice == "paper":
        return tie, str(computer_choice)
    if player_choice == "paper" and computer_choice == "scissors":
        return str(cwin), str(computer_choice)
    if player_choice == "paper" and computer_choice == "rock":
        return str(pwin), str(computer_choice)
    if player_choice == "scissors" and computer_choice == "paper":
        return str(pwin), str(computer_choice)
    if player_choice == "scissors" and computer_choice == "scissors":
        return tie, str(computer_choice)
    if player_choice == "scissors" and computer_choice == "rock":
        return str(cwin), str(computer_choice)


