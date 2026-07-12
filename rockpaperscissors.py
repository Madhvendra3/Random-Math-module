while True:
    useraction = input("enter choice(rock, paper, scissors)")
    actions = ("rock","paper","scissors")
    import random
    computeraction = random.choice(actions)
    print(f"\n you chose {useraction}, computer chose {computeraction}.\n")

    if useraction == computeraction:
        print(f"Both players selected {useraction}. It is a tie ")
    elif useraction == "rock":
        if computeraction == "scissors":
            print("Rock beats scissors, you win")    
        else:
            print("paper beats rock, you lose")
    elif useraction == "paper":
        if computeraction == "rock":
         print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif useraction == "scissors":
        if computeraction == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
#take input for playing again
    play_again = input("Play again? (you lose, y/n): ")
    if play_again != "y":
        break            

