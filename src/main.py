print("**********************************************************")
print(" Listen me. I want to play a game")
print(" You need choice between the numbers 0 and 100")
print(" Live or die, make your choice")
print("**********************************************************")

secret_number = 42

user_input = int(input("Digit a number: "))

if(user_input == secret_number):
    print("Congratz... You are the winner!")
else:
    print("HAHAHAHA... You lose!!!")

print("End game!")
