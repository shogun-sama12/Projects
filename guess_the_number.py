def try_to_guess_number():
    import random
    random_number=random.randint(1,100)
    print(f'random number is:{random_number}')
    attempt=0
    while True:
        try:
            guess=int(input('Try to guess number between 1 and 100: '))
            attempt+=1
        except ValueError:
            print('Enter a valid number')
            continue
        if guess==random_number:
            print(f'Congratulation! Total attemt:{attempt}')
        elif guess<random_number:
            print('To low')
        else:
            print('Too high')

try_to_guess_number()