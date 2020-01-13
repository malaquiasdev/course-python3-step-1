def play():
    print("**********************************************************")
    print(" Welcome to the Hangman Game u.u ")
    print("**********************************************************")

    secret_word = "banana"
    hanged = False
    win = False

    while(not win and not hanged):
        user_input = input(" Tell me a letter, please? ")

        index = 0
        for letter in secret_word:
            if(user_input.lower() == letter):
                print(f"We found the letter {letter} in the position {index}")
            index += 1

        print(" Playing...")

    print("**********************************************************")
    print(" You lose! T.T ")
    print("**********************************************************")


if(__name__ == "__main__"):
    play()
