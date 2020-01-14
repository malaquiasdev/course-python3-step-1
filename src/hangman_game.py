def user_input_is_equal_to_letter(user_input, letter):
    return user_input.lower().strip() == letter.lower().strip()


def game_loop(secret_word, hanged, win):
    while(not win and not hanged):
        user_input = input(" Tell me a letter, please? ")

        index = 0
        for letter in secret_word:
            if(user_input_is_equal_to_letter(user_input, letter)):
                print(f"We found the letter {letter} in the position {index}")
            index += 1

        print(" Playing...")


def play():
    print("**********************************************************")
    print(" Welcome to the Hangman Game u.u ")
    print("**********************************************************")

    secret_word = "banana"
    hanged = False
    win = False

    game_loop(secret_word, hanged, win)

    print("**********************************************************")
    print(" You lose! T.T ")
    print("**********************************************************")


if(__name__ == "__main__"):
    play()
