import random
x = random.randint(1,10)

number_to_be_guessed = x
guess_limit = 0
print(' ')
print('Maximum three guess only')
while guess_limit < 3:
    print(' ')
    guess = int(input("enter a number "))
    guess_limit += 1
    if guess == number_to_be_guessed:
        print(' ')
        print('congrats!!! you won :)')
        break
    print(' ')
    print(f'sorry...try again ..... {3 - guess_limit} remaining!!')
else:
    print(' ')
    print("Sorry ...you failed\n")
print(f"The random number was {x}")
print(' ')
input('press enter to exit')