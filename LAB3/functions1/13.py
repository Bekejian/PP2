import random
def pygame():
    print("Hello! What is your name?")
    name = input()

    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    
    secret_num = random.randint(1, 20)         #num = random.randint(1, 10) , output 这个区间的随机数字
    i = 0

    while True:
        print("\nTake a guess.")
        guess = int(input())
        i+= 1

        if guess < secret_num:
            print("\nYour guess is too low.")

        elif guess > secret_num:
            print("\nYour guess is too high.")

        else:
            print(f"\nGood job, {name}! You guessed my number in {i} guesses!")
            break

pygame()