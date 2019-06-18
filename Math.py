#Kids Math game because i am cheap
#Need to add Level of Difficulty
#Need to add limit level math (answer can not be greater than the max of level)
#Need to add for loops where need  X
#Need to add operations
#Need to add try except
#First program lets see what happens


import math
import random




i = 1
print('***********************************************************')
print('******************   NIEVES MATH GAME   *******************')
print('***********************************************************')
def addition():
    pass
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
        print('*                                                         *\n* GREAT JOB!!                                             *')
        print('*                                                         *')
        print('*                                                         *')
        print('*                                                         *')
    elif urans != ans:
        print('*                                                         *\n* Oh Oh!! Try Again Please.                               *')
        while urans != ans:
            urans = input('*    ')
            if urans == ans:
                print('*                                                         *\n* GREAT JOB!!                                             *')
                print('*                                                         *')
            elif urans != ans:
                print('*                                                         *\n* Oh Oh!! Try Again Please.                               *\n*')
    i = i+1
print('***********************************************************')


#cont = (input('* Do you want to keep Going?                              *\n')
#    if cont == 'Y' or 'Yes' or 'y' or 'yes':
#        i = 1
#    elif cont == 'N' or 'No' or 'n' or 'no':
print('*                  The Game is Over                        ')
print('***********************************************************')  
