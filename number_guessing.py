from sys import exit
from random import randint

def mini_game():
    game_ended=False
    attempts=10

    print("\nWelcome to the Number Guessing Game! 🤖")
    print("guess which number i'm thinking of... between 0 and 100.\n")

    computer_choice=randint(0,100)

    while attempts!=0:
        print("Attempts left:", attempts)
        while True:
            player_choice=int(input("Enter your guess\n"))
            if player_choice < 0 or player_choice > 100:
                print("\nplease respect the interval")
            else:
                break
            
        if player_choice == computer_choice:
            print(f"Congratulations, You won! 🎉\n")
            game_ended=True
            break
        elif player_choice > computer_choice:
            print(f"The number iam thinking of is lower")
        else:
            print(f"The number iam thinking of is higher\n")
        attempts-=1
        
    if(attempts==0):
        game_ended=True
        print("Game over! You've run out of attempts.\n")
        print(f"The correct number was {computer_choice}\n")
    if game_ended==True:
        while True:
            play_again=input(f"Play again?, \nY for Yes or\nQ to Quit\n")
            if play_again.lower() in ["y","q"]:
                break
        if play_again.lower()=="y":
            mini_game()
        else:
            if __name__ == "__main__":
                exit(f"\nThank you for playing!👋\n")
    

mini_game()