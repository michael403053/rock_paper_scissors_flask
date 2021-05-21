def win_finder(player1_choice, player2_choice):
    p1win = "Player 1 is the winner!"
    p2win = "Player 2 is the winner!"
    tie = "Tie Match!"
    if player1_choice == "rock" and player2_choice == "paper":
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