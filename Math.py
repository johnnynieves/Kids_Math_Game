#Kids Math game because i am cheap
#Need to add Level of Difficulty
#Need to add limit level math (answer can not be greater than the max of level)
#Need to add for loops where need  X
#Need to add operations
#Need to add try except
#First program lets see what happens


import math
import random


print('***********************************************************')
print('******************   NIEVES MATH GAME   *******************')
print('***********************************************************')
def add():
    print('addition')
    i = 1
    while i < 11:
        for i in range(1, 11):
            a = random.randint(0, 10)
            b = random.randint(0, 10)
            ans = a + b
            print('*                                                         *')
            print('*                                                         *')   
            print("*   Please enter your answer                              *")
            print('*                                                         *')
            print('*                                                         *')
            print("*     " + str(a) + "                                                   *")
            print("*    +" + str(b) + "                                                   *")
            print('* _________                                               *')
            urans = input('*    ')
            if urans == ans:
                print('*                                                         *\n*  GREAT JOB!!                                             *')
                print('*                                                         *')
                print('*                                                         *')
                print('*                                                         *')
            elif urans != ans:
                print('*                                                         *\n* Oh Oh!! Try Again Please.                               *')
                while urans != ans:
                    urans = input('*    ')
                    if urans == ans:
                        print('*                                                         *\n*  GREAT JOB!!                                            *')
                        print('*                                                         *')
                    elif urans != ans:
                        print('*                                                         *\n* Oh Oh!! Try Again Please.                               *\n*')
            i = i+1
        done = int(input('*  Do you want to continue to play?                       *\n*'))
        if done == 0:
            print("*  Good Bye                                               *")
            print('***********************************************************')
            print('*                  The Game is Over                       *')
            print('***********************************************************')  
        elif done == 1:
            i = 1
            print('***********************************************************')
            print('***************   Lets Continue Playing   *****************')
            print('***********************************************************')
            print('******************   NIEVES MATH GAME   *******************')
            print('***********************************************************')
            add()

def sub():
    print('subtraction')
    i = 1
    while i < 11:
        for i in range(1, 11):
            a = random.randint(0, 10)
            b = random.randint(0, 10)
            ans = a - b
            print('*                                                         *')
            print('*                                                         *')   
            print("*   Please enter your answer                              *")
            print('*                                                         *')
            print('*                                                         *')
            print("*     " + str(a) + "                                                   *")
            print("*    -" + str(b) + "                                                   *")
            print('* _________                                               *')
            urans = input('*    ')
            if urans == ans:
                print('*                                                         *\n*  GREAT JOB!!                                             *')
                print('*                                                         *')
                print('*                                                         *')
                print('*                                                         *')
            elif urans != ans:
                print('*                                                         *\n* Oh Oh!! Try Again Please.                               *')
                while urans != ans:
                    urans = input('*    ')
                    if urans == ans:
                        print('*                                                         *\n*  GREAT JOB!!                                            *')
                        print('*                                                         *')
                    elif urans != ans:
                        print('*                                                         *\n* Oh Oh!! Try Again Please.                               *\n*')
            i = i+1
        done = int(input('*  Do you want to continue to play?                       *\n*'))
        if done == 0:
            print("*  Good Bye                                               *")
            print('***********************************************************')
            print('*                  The Game is Over                       *')
            print('***********************************************************')  
        elif done == 1:
            i = 1
            print('***********************************************************')
            print('***************   Lets Continue Playing   *****************')
            print('***********************************************************')
            print('******************   NIEVES MATH GAME   *******************')
            print('***********************************************************')
            sub()

    ops = input('Select your operation 1 for addition, 2 for subtraction')
    if ops == 1:
        add()
    elif ops == 2:
        sub()
ops = input('1 for add, 2 for sub')
if ops == 1:
    add()
elif ops == 2:
    sub()
