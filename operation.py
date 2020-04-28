from time import time
from random import randint, choice


def add():
    counter = 0
    starttime = time()
    encouragement = [
        'Excellent',
        'Great',
        'Your Right',
        'Good Job',
        'Awesome',
        'Well Done'
        ]
    for i in range(0,10):
        first = randint(2,20)
        second = randint(2,first)
        if len(str(first)) == 2:
            print(f'  {first}')
        else:
            print(f'   {first}')
        if len(str(second)) == 2:
            print(f'_+{second}_')
        else:
            print(f'_+_{second}_')
        answer = first + second
        if len(str(answer)) == 2:
            try:
                my_answer = int(input('  '))
            except (ValueError,UnboundLocalError):
                print('We only accept numbers try again')
                my_answer = int(input('  '))
        else:
            try:
                my_answer = int(input('   '))
            except (ValueError,UnboundLocalError):
                print('We only accept numbers try again')
                my_answer = int(input('   '))
        if answer == my_answer:
            print(choice(encouragement) + '!!!')
            counter = counter + 1
        else:
            print('Oh! Oh!')
        print('\n')
    endtime = time()
    totaltime = starttime - endtime
    print(f'You got {counter} Right!')
    print(f'You took {abs(int(totaltime))} seconds')


def multi_add():
    counter = 0
    starttime = time()
    encouragement = [
        'Excellent',
        'Great',
        'Your Right',
        'Good Job',
        'Awesome',
        'Well Done'
        ]
    for i in range(0,10):
        first = randint(2,20)
        second = randint(2,first)
        third =  randint(2, second)
        if len(str(first)) == 2:
            print(f'  {first}')
        else:
            print(f'   {first}')

        if len(str(second)) == 2:
            print(f'  {second}')
        else:
            print(f'   {second}')

        if len(str(third)) == 2:
            print(f'_+{third}_')
        else:
            print(f'_+_{third}_')
        answer = first + second + third

        try:
            my_answer = int(input('  '))
        except (ValueError,UnboundLocalError):
            print('We only accept numbers try again')
            my_answer = int(input('  '))
        if answer == my_answer:
            print(choice(encouragement) + '!!!')
            counter = counter + 1
        else:
            print('Oh! Oh!')
        print('\n')
    endtime = time()
    totaltime = starttime - endtime
    print(f'You got {counter} Right!')
    print(f'You took {abs(int(totaltime))} seconds')


def subtraction():
    counter = 0
    starttime = time()
    encouragement = [
        'Excellent',
        'Great',
        'Your Right',
        'Good Job',
        'Awesome',
        'Well Done'
        ]
    for i in range(0,10):
        first = randint(2,20)
        second = randint(2,first)
        if len(str(first)) == 2:
            print(f'  {first}')
        else:
            print(f'   {first}')

        if len(str(second)) == 2:
            print(f'_-{second}_')
        else:
            print(f'_-_{second}_')
        answer = first - second
        try:
            my_answer = int(input('   '))
        except (ValueError,UnboundLocalError):
            print('We only accept numbers try again')
            my_answer = int(input('   '))
        if answer == my_answer:
            print(choice(encouragement) + '!!!')
            counter = counter + 1
        else:
            print('Oh! Oh!')
        print('\n')
    endtime = time()
    totaltime = starttime - endtime
    print(f'You got {counter} Right!')
    print(f'You took {abs(int(totaltime))} seconds')    