import random


user_guess = input("can you guess the number? ")
random_number = random.randint(1,10)
guess_count = 0


while user_guess != random_number:
    guess_count += 1
    print(user_guess)
else:
    print()
#This is just nice, the bravery is just to start

