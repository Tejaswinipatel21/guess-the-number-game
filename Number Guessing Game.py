import random
print("Number Gusseing Game")
no=random.randint(1,9)
chances=0
print("Guess a number between 1 to 9")
while chances <5:
    guess=int(input("Enter your guess"))
    if guess==no:
        print("Bravo!You Won")
        break
    elif guess<no:
        print("It's too low,Guess a number higher than", guess)
    else:
        print("It's too high,Guess a number lowerthan",guess)
    chances=chances+1    
