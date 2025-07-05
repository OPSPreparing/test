import random
def snake():

    player_input = input("Enter your choice (snake, gun, water, men, Q): ")
    choice = random.choice(["snake", "gun", "men", "water", "Q"])
    print("welcome to snake game")
    
    print(f"you choose {player_input} and computer choose {choice}")
    
    if player_input == choice:
        print("DRAW")
    elif player_input == "gun" and choice == "snake":
        print("WON")
    elif player_input == "gun" and choice == "men":
        print("WON")
    elif player_input == "gun" and choice == "water":
        print("LOST")
    elif player_input == "snake" and choice == "water":
        print("WON")
    elif player_input == "snake" and choice == "men":
        print("WON")
    elif player_input == "men" and choice == "water":
        print("WON")
    elif player_input == "Q":
        print("Quit")
    else:
        print("input is different")

snake()
