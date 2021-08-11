'''
Number Forecast App

'''

import random   # add random module

chances = 5 # gamer has got 3 changes

random_number = random.randint(1,3)   # 1-100 create random number
counter = 0

print('ATTENTİON\nFor Forcast App you got 3 chances !')

while chances > 0:
    chances -=1
    counter +=1
    forecast = int(input('Forecast: ')) # from gamer send request for forecast

    if random_number == forecast:
        print(f'Congrats !. {counter}nd time you found. The number was: {random_number}')
        break
    elif random_number > forecast:
        print(f'Up. {counter}nd used.')
    else:
        print(f'Down. {counter}nd used.')
    if chances == 0:
        print(f'You right is over. The number was: {random_number}')
        print(f'You have {counter-3} chances.')
    
    




    
