def user_input_is_equal_to_letter(user_input, letter):
    return user_input == letter


def is_the_user_hanged(number_of_errors):
    return number_of_errors == 6


def game_loop(secret_word, user_hit_letters):
    win = False
    number_of_errors = 0
    print(f'Hit letters {user_hit_letters}')
    while not win and not is_the_user_hanged(number_of_errors):
        user_input = input(" Tell me a letter, please? ").lower().strip()
        index = 0
        if user_input in secret_word:
            for letter in secret_word:
                if user_input_is_equal_to_letter(user_input, letter):
                    user_hit_letters[index] = letter
                index += 1
        else:
            number_of_errors += 1
        print(user_hit_letters)


def play():
    print("**********************************************************")
    print(" Welcome to the Hangman Game u.u ")
    print("**********************************************************")

    secret_word = "banana".lower().strip()
    user_hit_letters = ["_", "_", "_", "_", "_", "_"]

    game_loop(secret_word, user_hit_letters)

    print("**********************************************************")
    print(" You lose! T.T ")
    print("**********************************************************")


if (__name__ == "__main__"):
    play()
