import random

def get_number_input():
    while True:
        user_input = input('Enter your guess: ')
        try:
            number = int(user_input)
            return number
        except ValueError:
            print('Please enter a valid number!')

def play_game():
    while True:
        print('''This is a Guess The Number Game!
I am thinking of a number between 1 and 100.
Can you guess what it is?''')
        n = random.randint(1,100)
        attempts = 0
        a = get_number_input()
        while a!=n:
            attempts += 1
            if a>n:
                print('Your guess is too high!')
            else:
                print('Your guess is too low!')
            a = get_number_input()
        print(f'Congratulations! You guessed the number correctly in {attempts} attempts!')
        break

def main():
    while True:
        play_game()
        pa = input('Do you wsnt to play again? (yes/no): ').lower()
        if pa != 'yes':
            break


if __name__ == '__main__':
    main()