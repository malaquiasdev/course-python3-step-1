from src import enigma
from src import hangman_game

def choose_game():
    print("*********************************")
    print("******* Choose your game! *******")
    print("*********************************")

    print("(1) Enigma (2) Hangman Game")

    jogo = int(input(" What is your choice? "))

    if(jogo == 1):
        print("Starting the enigma")
        enigma.play()
    elif(jogo == 2):
        print("Starting the Hangman Game")
        hangman_game.play()


if(__name__ == "__main__"):
    choose_game()
