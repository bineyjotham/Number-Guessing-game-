import random

top_of_range = input("Type a number to be the maximum range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number that is bigger than 0 next time!")
        quit()

r = random.randrange(0, top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please type a number next time!")
        continue

    if user_guess == r:
        print("You got it correct!")
        break
    elif user_guess < r:
        print("You got it wrong!")
        print("The number is greater than your input!")
    else:
        print("You got it wrong!")
        print("The number is less than your input!")

print("You got it in", guesses, "guesses")
