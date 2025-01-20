'''
project_1.py: First project for Engeto Online Python Akademie

 author: Marta Martinkova
 email: marta@ufa.cas.cz
'''
import random

def generating_4digit_number():
    '''
    Generating a random 4-digit number with unique digits.
    '''
    digits = list(range(10))
    random.shuffle(digits)
    # Ensuring that the first digit is not 0
    while digits[0] == 0:
        random.shuffle(digits)
    return ''.join(map(str, digits[:4]))

def get_feedback(secret, guess):
    '''
    Calculate the number of bulls and cows for a given guess.
    '''
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), 
                   guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

def is_valid_guess(guess):
    '''
    Check if the guess is a valid 4-digit number with unique digits 
    and not starting with 0.
    '''
    if len(guess) != 4 or not guess.isdigit():
        return False
    if guess[0] == '0':
        return False
    if len(set(guess)) != 4:
        return False
    return True


def bulls_and_cows_game():
    '''
    Main game logic.
    '''
    print(f'Hi there!')
    print('_' * 47)
    print(f'I\'ve generated a random 4 digit number for you.')
    print(f'Let\'s play a bulls and cows game.')
    print('_' * 47)
    print('Enter a number: ')

    secret_number = generating_4digit_number()

    attempts = 0

    while True:
              
        print('_' * 47)
        guess = input().strip()
        if not is_valid_guess(guess):
            print(f'Invalid input. Please enter ' + \
                  'a 4-digit number \nwith unique digits ' + \
                  'that does not start with 0.')
            continue

        attempts += 1
        bulls, cows = get_feedback(secret_number, guess)

        bulls_text = 'bull' if bulls == 1 else 'bulls'
        cows_text = 'cow' if cows == 1 else 'cows'
        print(f'{bulls} {bulls_text}, {cows} {cows_text}')

        if bulls == 4:
            print(f'Correct, you\'ve guessed the right number')
            print(f'in {attempts} guesses!')
            print('_' * 47)
            print('That\'s amazing!')
            break


if __name__ == '__main__':
    bulls_and_cows_game()
