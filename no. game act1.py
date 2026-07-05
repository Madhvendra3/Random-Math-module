import random
playing = True
number = str(random.randint(0,3))
print("I will generate no. from 0-10 & you have to guess it.")
print("the game ends when you get 1 same no. as me.")
while playing:
    guess = input("give me your guess: \n")
    if number == guess:
        print("You win")
        print("The number was",number)
        break
    else:
        print("Please try again.")    