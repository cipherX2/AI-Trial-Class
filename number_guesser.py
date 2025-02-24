def number_guesser():
    """This function helps to guess a number from the range of 1 to 10"""
    """This is a simple example of binary search...."""

    name = input("Hi - What is your name ? ")
    print(f"Nice to meet you, {name}")

    low = int(input(f"{name}, what is the lowest number I should guess ? "))
    high = int(input(f"And what is the highest number I should guess ? "))
    attempts = 0

    print(f"Welcome to Number Guesser Game, {name}")
    print(f"Think of a number between {low} and {high} and I'll try to guess it!")

    input("Press Enter to start the game")

    while low <= high:
        guess = (low + high) // 2
        attempts += 1

        print(f"My guess is {guess}")
        feedback = input("If correct press 'c', Press 'h' to guess higher and Press 'l' to guess lower ").lower()

        if feedback == "c":
            print(f"Yay! I guessed the number correct in only the {attempts} attempts!")
            break
        elif feedback == "h":
            low  = guess + 1
            print("I'll guess higher now......")
        elif feedback == "l":
            high = guess - 1

    if low > high:
        print(f"I think there is something wrong....., {name}. Are you sure you followed the rules? ")



number_guesser()