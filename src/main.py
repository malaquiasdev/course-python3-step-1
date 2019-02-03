print("**********************************************************")
print(" Listen me. I need you to cooperate with me, let's play?")
print("**********************************************************")

secret_number = 42

user_input = int(input("Digit a number: "))

if(user_input == secret_number):
    print("Congratz... You are the winner!")
else:
    print("HAHAHAHA... You lose!!!")
