secret_number = 5


def game():
    while True:
        guess_number = int(input("Please,guess number between 1 and 10"))
        if guess_number is str:
            print("type number please")
            guess_number = int(input("Please,guess number between 1 and 10"))
        if guess_number == secret_number:
            print("Correct!")
            break
        elif guess_number < secret_number:
            print("Too low")
        elif guess_number > secret_number:
            print("Too high")

        else:
            print("Sorry Something went wrong")


game()
another_try = input("Do you want to try again?")
while another_try == "yes":
    game()
    another_try = input("Do you want to try again?")

if another_try == "no":
    print("Goodbye")
