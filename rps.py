import random

alow = ['rock', 'paper', 'scissors']

def enter_choice():
    while True:
        user_input = input().lower()
        if user_input in alow:
            return user_input
        else:
            print('Please enter a valid chioce!')
        
def play_game():
    print('This is rock-paper-scissors game!')
    print('Enter your choice: rock, paper, or scissors')
    a = enter_choice()
    b = random.choice(alow)
    print(f'Your choice: {a}')
    print(f'Computer choice: {b}')
    if a == b:
        print('Draw!')
    elif (a == 'rock' and b == 'scissors') or (a =='paper' and b == 'rock') or (a == 'scissors' and b == 'paper'):
        print('You win!')
    else:
        print('You lose!')
    

def main():
    play_game()
    while True:
        retry = input('Do you want to play again? (yes/no):').lower()
        if retry == 'yes':
            play_game()
        else:
            break

        
        

if __name__ == '__main__':
    main()