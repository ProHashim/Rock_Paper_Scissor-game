import sys

user_1 = input('What is your name? ').upper()
user_2 = input('Your name, user 2? ').upper()

#.format is used to to format string, 
# .format can be used as in below line of code
user_1_answer = input('what do you want to choose {}? '.format(user_1)).upper()

# %s is also used to format strings. We can use
# the %s, can be used like below line of code
user_2_answer = input('%s, What do you want to  choose?' % user_2).upper()


def compare(user_one, user_two):
    if user_one == user_two:
        return('it is tie!')
    elif user_one == 'ROCK':
        if user_two == 'PAPER':
            return ('Rock wins')
        else:
            return ('paper wins')
    elif user_one == 'SCISSORS':
        if user_two == 'PAPER':
            return('Scissors win')
        else:
            return('Rock wins')

    
    elif user_one == 'PAPER':
        if user_two == 'ROCK':
            return('Paper wins! ')
        else:
            return('Scissors wins! ')
    
    else:
        return('Invalid input!  You entered the wrong input')
        sys.exit()


print(compare(user_1_answer, user_2_answer))