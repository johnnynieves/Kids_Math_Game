#Kids Math game because i am cheap

#   Need to add Level of Difficulty
# X Need to add limit level math (answer can not be greater than the max of level) (Dumb dont need this) 
# X Need to add for loops where need  
# x Need to add operations 
# X Need to add try except  -  (also need them in the functions)
#   First program lets see what happens

import math
from random import randint

#Addition Function
def add():
    for i in range(0,11):
        a = randint(0, 10)
        b = randint(0, 10)
        right_ans = a + b
        print('*'+' ' * 78 + '*')
        print('*'+' ' * 78 + '*')   
        print("*" + ' ' * 3 + 'Please enter your answer' + ' ' * 51 + '*')
        print('*'+' ' * 78 + '*')
        print('*'+' ' * 78 + '*')
        print("*" + ' ' * 5 + str(a) + " " * 72 + '*')
        print("*" + ' ' * 4 +'+' + str(b) + " " * 72 + '*')
        print('* _________' + ' ' * 68 + '*')

        urans = int(input('*' + ' ' * 5))
        if urans == right_ans:
            print('*'+' ' * 78 + '*')    
            print('*  GREAT JOB!!' + ' ' * 65 + '*')
            print('*'+' ' * 78 + '*')
            print('*'+' ' * 78 + '*')
            print('*'+' ' * 78 + '*')
  
        if urans != right_ans:
            print('*'+' ' * 78 + '*')
            print('* Oh Oh!! Try Again Please.' + ' ' * 32 + '*')
            while urans != right_ans:
                urans = int(input('*' + ' ' * 5))
                if urans == right_ans:
                    print('*'+' ' * 78 + '*')    
                    print('*  GREAT JOB!!' + ' ' * 65 + '*')
                    print('*'+' ' * 78 + '*')
                    print('*'+' ' * 78 + '*')
                    print('*'+' ' * 78 + '*')
                
        ask()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Subtraction Function
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def sub():
    for i in range(0,5):
        a = random.randint(10, 20)
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
        urans = int(input('*     '))
        if urans == ans:
            print('*                                                         *\n*  GREAT JOB!!                                            *')
            print('*                                                         *')
            print('*                                                         *')
            print('*                                                         *')
        elif urans != ans:
           print('*                                                         *\n* Oh Oh!! Try Again Please.                               *')
           while urans != ans:
                urans = int(input('*    '))
                if urans == ans:
                    print('*                                                         *\n*  GREAT JOB!!                                            *')
                    print('*                                                         *')
        ask()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Continue ???
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def ask():
    done = int(input('*  Do you want to continue to play?' + ' ' * 44 + '*\n*  0 to exit 1 to continue' + ' ' * 53 + '*\n*  >_'))
    try:
        if done is 0:
            exit()
        ops = int(input('*   Select your operation 1 for addition, 2 for subtraction ' + ' ' * 19 + '*\n*   '))
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
        elif done != 0 or 1 or 2: 
            print('Try again')
    except SystemError:
        
        print('something went wrong')

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\    
#Main Program
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def main():
    print('*' * 80)
    print('*' + ' ' * 28 + '   NIEVES MATH GAME   ' + ' ' * 28 + '*')
    print('*' * 80)
    


    ops = int(input('*   Select your operation 1 for addition, 2 for subtraction ' + ' ' * 19 + '*\n*   '))
    try:
        if ops == 1:
            add()
        elif ops == 2:
            sub()
    except ValueError:
        print('* \n* Please enter a number.')
       
if __name__ == "__main__":
    main()