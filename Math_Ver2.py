import math
from time import time
from random import randint


def add():
    counter = 0
    starttime = time()
    for i in range(0,10):
        first = randint(0,10)
        second = randint(0,10)
        answer = first + second
        print(f'   {first}')
        print(f'_+_{second}_')
        
        try:
            my_answer = int(input('   '))
        except (ValueError,UnboundLocalError):
            print('We only accept numbers try again')
            my_answer = int(input('   '))

        if answer == my_answer:
            print('Your Right!!!')
            counter = counter + 1
        else:
            print('Oh! Oh!')
        print('\n')
    endtime = time()
    totaltime = starttime - endtime
    print(f'You got {counter} Right!')
    print(f'You took {abs(int(totaltime))} seconds')    


if __name__ == "__main__":
    add()