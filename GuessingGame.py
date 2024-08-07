import random

def get():
    return random.randrange(1, 50)

def guess_num(msg):
    return eval(input(f'{msg}: '))

def guess(num):
    guessed = guess_num('Try within the range of 1 to 50')
    while guessed!=num:
        if guessed> num:
            guessed = guess_num('Try with smaller Number')
        else:
            guessed = guess_num('Try with larger Number')
    return f"Yuhooo!!! Your Guess is correct. The number is {guessed}"

num = get()
print(guess(num))
