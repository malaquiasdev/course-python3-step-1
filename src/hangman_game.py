def user_input_is_equal_to_letter(user_input, letter):
    return user_input == letter


def is_the_user_hanged(number_of_errors, limit_of_attempts):
    return number_of_errors == limit_of_attempts


def have_we_a_winner(user_hit_letters):
    return "_" not in user_hit_letters


def game_loop(secret_word, user_hit_letters):
    limit_of_attempts = 6
    number_of_errors = 0
    print(f'Hit letters {user_hit_letters}')
    while not have_we_a_winner(user_hit_letters) and not is_the_user_hanged(number_of_errors, limit_of_attempts):
        user_input = input(" Tell me a letter, please? ").lower().strip()
        index = 0
        if user_input in secret_word:
            for letter in secret_word:
                if user_input_is_equal_to_letter(user_input, letter):
                    user_hit_letters[index] = letter
                index += 1
        else:
            number_of_errors += 1
            print(f'Oops, you missed! There are {limit_of_attempts - number_of_errors} attempts left.')
        print(user_hit_letters)
    return {'number_of_errors': number_of_errors, 'user_hit_letters': user_hit_letters}


def play():
    print("**********************************************************")
    print(" Welcome to the Hangman Game u.u ")
    print("**********************************************************")

    secret_word = "banana".lower().strip()
    user_hit_letters = ["_" for letter in secret_word]

    result = game_loop(secret_word, user_hit_letters)

    if have_we_a_winner(result['user_hit_letters']):
        print("**********************************************************")
        print("You are the WINNER !!! \o/")
        print("**********************************************************")
    else:
        print("**********************************************************")
        print(" You lose! T.T ")
        print("**********************************************************")


if (__name__ == "__main__"):
    play()
