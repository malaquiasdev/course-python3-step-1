def user_input_is_equal_to_letter(user_input, letter):
    return user_input.lower().strip() == letter.lower().strip()


def game_loop(secret_word, user_hit_letters, hanged, win):
    print(f'Hit letters {user_hit_letters}')
    while(not win and not hanged):
        user_input = input(" Tell me a letter, please? ")
        index = 0
        for letter in secret_word:
            if(user_input_is_equal_to_letter(user_input, letter)):
                user_hit_letters[index] = letter
            index += 1
        print(user_hit_letters)


def play():
    print("**********************************************************")
    print(" Welcome to the Hangman Game u.u ")
    print("**********************************************************")
    
    secret_word = "banana"
    user_hit_letters = ["_", "_", "_", "_", "_", "_"]
    hanged = False
    win = False

    game_loop(secret_word, user_hit_letters, hanged, win)

    print("**********************************************************")
    print(" You lose! T.T ")
    print("**********************************************************")


if(__name__ == "__main__"):
    play()
