# Make a PIG Game! 

import random

def roll():
    r = random.randint(1, 6)
    return r

while True:
    players = input("Enter the number of Players (2-4): ")

    if players.isdigit():
        players = int(players)
        if not (2 <= players <= 4):
            print("Players should be between 2-4")
            continue
        break
    else:
        print("Invalid Input! ")

max_score = 50
players_names = ["" for _ in range(players)]
players_score = [0 for _ in range(players)]

for i in range (len(players_names)):
    name = input(f"Enter the name for Player {i+1}: ")
    players_names[i] += name

while (max(players_score) < max_score):

    for player_ind in range(players):
        print()
        print(f"    {players_names[player_ind]}'s turn started...")
        print(f"    Total Score is {players_score[player_ind]}.\n")
        
        current_score = 0 
        while True:
            is_ready = input("Roll the Dice? (Y or N) ").lower()
            if (is_ready != 'y'):
                if (is_ready == 'n'):
                    break
                else:
                    print("Invalid Input! ")
                    continue
            r = roll()
            if r == 1:
                print("You got 1")
                print("Your score is reset to 0")
                players_score[player_ind] = 0
                break
            else:
                print(f"You get {r}")
                players_score[player_ind] += r
                current_score += r
                print(f"Your current score is {current_score}") 
                
            if players_score[player_ind] >= max_score:
                print("ALERT 🚩 You have got the maximum score. Now if you roll again and score 1, your total score will be reset to 0") 
              
        if players_score[player_ind] >= max_score:
            break

max_value = max(players_score)
winner_ind = players_score.index(max_value)
print(f"\nCongratulations to {players_names[winner_ind]} who has won with the score {max_value}\n")