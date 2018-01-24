number = 23
running = True

while running:
    guess = int(input('enter an integer :'))

    if guess == number:
        print('success!,you guessed it.')
        running = False
    elif guess<number:
        print('No,it is little higher!')
    else:
        print('No,it is little lower!')
else:
    print('The while loop is over.')

print('done')