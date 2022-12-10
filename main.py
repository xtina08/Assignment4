from random import randint

colors = ['red', 'blue', 'black', 'pink', 'green', 'yellow']
generator = randint(0, len(colors) - 1)
guess = input('Guess the random color: ')

for color in colors[generator]:
    if guess != colors[generator]:
        print('Wrong, try again')
        guess = input('Guess the color: ')
    elif guess == colors[generator]:
        break

print('Yay!, you guessed the color correct. It was: ' + colors[generator])
