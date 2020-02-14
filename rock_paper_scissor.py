import sys

user_1 = input('What is your name? ').upper()
user_2 = input('Your name, user 2? ').upper()

#.format is used to to format string, 
# .format can be used as in below line of code
user_1_answer = input('what do you want to choose {}? '.format(user_1)).upper()

# %s is also used to format strings. We can use
# the %s, can be used like below line of code
user_2_answer = input('%s, What do you want to  choose?' % user_2).upper()


def compare(u1, u2):
    if u1 == u2:
        return('it is tie!')
    elif u1 == 'ROCK':
        if u2 == 'PAPER':
            return ('Rock wins')
        else:
            return ('paper wins')
    elif u1 == 'SCISSORS':
        if u2 == 'PAPER':
            return('Scissors win')
        else:
            return('Rock wins')

    
    elif u1 == 'PAPER':
        if u2 == 'ROCK':
            return('Paper wins! ')
        else:
            return('Scissors wins! ')
    
    else:
        return('Invalid input!  You entered the wrong input')
        sys.exit()


print(compare(user_1_answer, user_2_answer))