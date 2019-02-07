print("**********************************************************")
print(" Listen me. I want to play a game")
print(" You need choice between the numbers 0 and 100")
print(" Make your choice !!!")
print("**********************************************************")

secret_number = 42
attempts_total = 3

for attempt in range(1, attempts_total + 1):
    print("Attempt {} of {}".format(attempt, attempts_total))

    user_input = int(input("Digit a number: "))

    if(user_input < 1 or user_input > 100):
        print("You must enter a number between 1 and 100!")
        continue

    is_equal_than_secret_number = user_input == secret_number
    is_greater_than_secret_number= user_input > secret_number
    is_smaller_than_secret_number = user_input < secret_number

    if(is_equal_than_secret_number):
        print("Congratz... You are the winner!")
        break
    else:
        if(is_greater_than_secret_number):
            print("You missed! Your number is greater than the secret number!")
        elif(is_smaller_than_secret_number):
            print("You missed! Your number is smaller than the secret number!")

print("End game!")
