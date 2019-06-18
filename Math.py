#Kids Math game because i am cheap
#Need to add Level of Difficulty
#Need to add limit level math (answer can not be greater than the max of level)
#Need to add for loops where need 
#Need to add operations
#Need to add try except
#First program lets see what happens

import math
import random
a = random.randint(0, 10)
b = random.randint(0, 10)
ans = a + b
print('***********************************************************')
print('******************   NIEVES MATH GAME   *******************')
print('*********************************************************** \n')

print("Please enter your answer \n")
print(" " + str(a))
print("+" + str(b))
print('_______')
urans = input()
if urans == ans:
    print('GREAT JOB!!')
elif urans != ans:
    print('Oh Oh!! Try Again Please.')
