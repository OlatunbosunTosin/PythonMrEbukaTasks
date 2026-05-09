player_1 = input("Scissor, Rock or Paper: ")
player_2 = input("Scissor, Rock or Paper: ")


if player_1.lower() == "scissors" and player_2.lower() == "scissors" or player_1.lower() == "rock" and player_2.lower() == "rock" or player_1.lower() == "paper" and player_2.lower() == "paper":
    print("Tie\n")

elif player_1.lower() == "scissors" and player_2.lower() == "paper" or player_1.lower() == "paper" and player_2.lower() == "rock" or player_1.lower() == "rock" and player_2.lower() == "scissors":
    print("Player 1 wins\n")

elif player_1.lower() == "paper" and player_2.lower() == "scissors" or player_1.lower() == "rock" and player_2.lower() == "paper" or player_1.lower() == "scissors" and player_2.lower() == "rock":
    print("Player 2 wins\n")

else:
    print("invalid\n")
