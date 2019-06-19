#Kids Math game because i am cheap

#   Need to add Level of Difficulty
# X Need to add limit level math (answer can not be greater than the max of level) (Dumb dont need this) 
# X Need to add for loops where need  
# x Need to add operations 
# X Need to add try except  -  (also need them in the functions)
#   First program lets see what happens


import math
import random


#Addition Function
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def add():
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
                print('*                                                         *\n*  GREAT JOB!!                                            *')
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
    ask()


def ask():
    done = int(input('*  Do you want to continue to play?                       *\n*  0 to exit 1 to continue                                *\n*  '))
    try:
        if done == 0:
            ops = int(input('*                                                         *\n* Select your operation 1 for addition, 2 for subtraction *\n* '))
            if done == 1 and ops == 1:
                print('***********************************************************')
                print('***************   Lets Continue Playing   *****************')
                print('***********************************************************')
                print('******************   NIEVES MATH GAME   *******************')
                print('***********************************************************')
                add()
            elif done == 1 and ops == 2:
                print('***********************************************************')
                print('***************   Lets Continue Playing   *****************')
                print('***********************************************************')
                print('******************   NIEVES MATH GAME   *******************')
                print('***********************************************************')
                sub()
        
        print("*  Good Bye !!!                                           *")
        print('***********************************************************')
        print('*                  The Game is Over                       *')
        print('***********************************************************')
        exit()  
    except:
        print('something went wrong')


#Subtraction Function
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def sub():
    i = 1
    while i < 11:
        for i in range(1, 11):
            a = random.randint(10, 20)
            b = random.randint(0, 10)
            ans = a - b
            print('*                                                         *')
            print('*                                                         *')   
            print("*   Please enter your answer                              *")
            print('*                                                         *')
            print('*                                                         *')
            print("*      " + str(a) + "                                                 *")
            print("*    - " + str(b) + "                                                  *")
            print('* _________                                               *')
            urans = input('*      ')
            if urans == ans:
                print('*                                                         *\n*  GREAT JOB!!                                            *')
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
                        print('*                                                         *\n* Oh Oh!! Try Again Please.                               *\n*  ')
            i = i+1
        done = int(input('*  Do you want to continue to play?                       *\n*  0 to exit 1 to continue                                *\n*  '))
        ops = int(input('*                                                         *\n* Select your operation 1 for addition, 2 for subtraction *\n* '))
        if done == 0:
            print("*  Good Bye                                               *")
            print('***********************************************************')
            print('*                  The Game is Over                       *')
            print('***********************************************************') 
            exit() 
        elif done == 1 and ops == 2:
            i = 1
            print('***********************************************************')
            print('***************   Lets Continue Playing   *****************')
            print('***********************************************************')
            print('******************   NIEVES MATH GAME   *******************')
            print('***********************************************************')
            sub()
        elif done == 1 and ops == 1:
            add()
    
#Main Program
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#Main():
print('***********************************************************')
print('******************   NIEVES MATH GAME   *******************')
print('***********************************************************')
ops = int(input('*                                                         *\n* Select your operation 1 for addition, 2 for subtraction *\n* '))
while ops != 1 or 2 or 0:
    try:
        if ops == 1:
            add()
        elif ops == 2:
            sub()
        elif ops == 0:
            break
    #            else:
    #                ops = int(input('*                                                         *\n* Select your operation 1 for addition, 2 for subtraction *\n'))
    except:
        print('* \n* Please enter a number.')
       