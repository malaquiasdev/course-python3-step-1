import random


def get_hangman_game_secret_word_list():
    file = open('src/hangman_game_secret_word_list.txt', 'r')
    secret_words = [line.lower().strip() for line in file]
    file.close()
    return secret_words


def get_secret_word():
    secret_words = get_hangman_game_secret_word_list()
    random_word_position = random.randrange(0, len(secret_words))
    return secret_words[random_word_position]


def user_input_is_equal_to_letter(user_input, letter):
    return user_input == letter


def is_the_user_hanged(number_of_errors, limit_of_attempts):
    return number_of_errors == limit_of_attempts


def have_we_a_winner(hit_letters_mask):
    return "_" not in hit_letters_mask


def game_loop(secret_word, hit_letters_mask):
    limit_of_attempts = 6
    number_of_errors = 0
    print(f'Hit letters {hit_letters_mask}')
    while not have_we_a_winner(hit_letters_mask) and not is_the_user_hanged(number_of_errors, limit_of_attempts):
        user_input = input(" Tell me a letter, please? ").lower().strip()
        index = 0
        if user_input in secret_word:
            for letter in secret_word:
                if user_input_is_equal_to_letter(user_input, letter):
                    hit_letters_mask[index] = letter
                index += 1
        else:
            number_of_errors += 1
            print(f'Oops, you missed! There are {limit_of_attempts - number_of_errors} attempts left.')
        print(hit_letters_mask)
    return {'number_of_errors': number_of_errors, 'hit_letters_mask': hit_letters_mask}


def play():
    print("**********************************************************")
    print(" Welcome to the Hangman Game u.u ")
    print("**********************************************************")

    secret_word = get_secret_word()
    hit_letters_mask = ["_" for letter in secret_word]

    result = game_loop(secret_word, hit_letters_mask)

    if have_we_a_winner(result['hit_letters_mask']):
        print("**********************************************************")
        print("You are the WINNER !!! \o/")
        print("**********************************************************")
    else:
        print("**********************************************************")
        print(" You lose! T.T ")
        print("**********************************************************")


if (__name__ == "__main__"):
    play()
