import random

f = open('passwords.txt','a')

def password_generator(n):
    ps = ''
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
    for i in range(n):
        ps += random.choice(characters)
    return ps

def generator(n):
    password = password_generator(n)
    print('Your password is: ',password)
    return password

def save_password(tag,password):
    f.write(tag + ' : ' + password + '\n')
    f.close()

def main():
    n = int(input('Hello, this is a password generator, how many characters do you want the password?: '))
    password = generator(n)
    while True:
        answer = input('Do you want another password? (yes/no):').lower()
        if answer == 'yes':
            password = generator(n)
        else:
            tag = input('Which tag do you want to save the password with?:')
            save_password(tag,password)
            print('Thank you for using the password generator!')
            break
if __name__ == '__main__':
    main()