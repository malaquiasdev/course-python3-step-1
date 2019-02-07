import random

print("**********************************************************")
print(" Listen me. I want to play a game")
print(" You need choice between the numbers 0 and 100")
print(" Make your choice !!!")
print("**********************************************************")

secret_number = random.randrange(1, 101)
attempts_total = 0
user_points = 1000

print("Select a difficulty level for your match")
match_level = int(input("(1) Easy, (2) Medium, (3) Hard"))

if(match_level == 1):
    attempts_total = 20
elif(match_level == 2):
    attempts_total = 10
else:
    attempts_total = 5

for attempt in range(1, attempts_total + 1):
    print(f"Attempt {attempt} of {attempts_total}")

    user_input = int(input("Digit a number: "))

    if(user_input < 1 or user_input > 100):
        print("You must enter a number between 1 and 100!")
        continue

    is_equal_than_secret_number = user_input == secret_number
    is_greater_than_secret_number= user_input > secret_number
    is_smaller_than_secret_number = user_input < secret_number

    if(is_equal_than_secret_number):
        print(f"Congratz... You are the winner! Your scored is {user_points}.")
        break
    else:
        if(is_greater_than_secret_number):
            print("You missed! Your number is greater than the secret number!")
        elif(is_smaller_than_secret_number):
            print("You missed! Your number is smaller than the secret number!")
        lost_points = abs(secret_number - user_input)
        user_points = user_points - lost_points

print("End game!")
