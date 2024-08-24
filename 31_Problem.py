# Make a SNAKE WATER GUN Game! 

import random
import time

def SWG_Game ():
    user_name = input("\nEnter your name before we continue: ")
    print(f"Hi {user_name}, Welcome to SNAKE WATER GUN! ")
    is_ready = input("Are you READY to Play? (YES) or (NO): ")

    if is_ready.lower() == "yes":
        while(True):
            my_choice = ''
            rand_no: int = random.randint(1, 4)
            if rand_no == 1:
                my_choice = "snake"
            elif rand_no == 2:
                my_choice = "water"
            else:
                my_choice = "gun"

            print("""
    You will have to choose one from the following:
    1. Snake
    2. Water
    3. Gun
                """)
            user_choice = input("Enter your choice (1 OR 2 OR 3): ")
            if user_choice == '1':
                user_choice = "snake"
            elif user_choice == '2':
                user_choice = "water"
            else:
                user_choice = "gun"

            if user_choice == 'snake' and my_choice == 'water':
                print(f"Computer chose {my_choice.upper()} and you chose {user_choice.upper()}")
                print("You WIN! Snake drank the Water")
            elif user_choice == 'water' and my_choice == 'snake': 
                print(f"Computer chose {my_choice.upper()} and you chose {user_choice.upper()}")
                print("You LOST! Snake drank the Water")
            elif user_choice == 'water' and my_choice == 'gun':
                print(f"Computer chose {my_choice.upper()} and you chose {user_choice.upper()}")
                print("You WIN! Gun drown in Water")
            elif user_choice == 'gun' and my_choice == 'water':
                print(f"Computer chose {my_choice.upper()} and you chose {user_choice.upper()}")
                print("You LOST! Gun drown in Water")
            elif user_choice == 'gun' and my_choice == 'snake':
                print(f"Computer chose {my_choice.upper()} and you chose {user_choice.upper()}")
                print("You WIN! Gun Kills the Snake")
            elif user_choice == 'snake' and my_choice == 'gun':
                print(f"Computer chose {my_choice.upper()} and you chose {user_choice.upper()}")
                print("You LOST! Gun Kills the Snake")
            elif user_choice == my_choice:
                print(f"GAME DRAW! Both chose {user_choice.upper()}")
            else:
                print("Invalid Choice! ")
            play_again = input("\nPlay Again? Enter YES or No: ")
            if (play_again.lower() != 'yes'):
                print("Exiting...")
                time.sleep(1)
                return
            
    else:
        print("Exiting...")
        time.sleep(1)
        return


SWG_Game()