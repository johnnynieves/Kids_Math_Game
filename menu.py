from operation import add, multi_add, subtraction
import os

def console():
    print('*' * 80)
    print('*' + ' ' * 28 + '   NIEVES MATH GAME   ' + ' ' * 28 + '*')
    print('*' * 80)
    print()
    ops = int(input('''
    * Select your operation:

    * 1 for addition
    * 2 for multiple addition
    * 3 for subtraction
    
    \n> '''))
    print('*' * 80,'\n')
    try:
        if ops == 1:
            os.system('clear')
            print('*' * 80)
            print('*' + ' ' * 28 + '   READY SET GO!!!!   ' + ' ' * 28 + '*')
            print('*' * 80,'\n')
            add()
        elif ops == 2:
            os.system('clear')
            print('*' * 80)
            print('*' + ' ' * 28 + '   READY SET GO!!!!   ' + ' ' * 28 + '*')
            print('*' * 80,'\n')
            multi_add()
        elif ops == 3:
            os.system('clear')
            print('*' * 80)
            print('*' + ' ' * 28 + '   READY SET GO!!!!   ' + ' ' * 28 + '*')
            print('*' * 80,'\n')
            subtraction()
        else:
            print('* \n* Please enter a 1 for addition, 2 for subtraction.')
            console()    
    except ValueError:
        print('* \n* Please enter a number.')


    
def ask():
    print('*' * 80)
    done = int(input(
        '*  Do you want to continue to play?' +
        ' ' * 44 + '*\n*  0 to exit 1 to continue' +
        ' ' * 53 + '*\n*  >_'))
    try:
        if done is 0:
            exit()
        print('*' * 80)
        ops = int(input('*   Select your operation 1 for addition, 2 for subtraction ' + ' ' * 19 + '*\n*   '))
        if done == 1 and ops == 1:
            print('***********************************************************')
            print('***************   Lets Continue Playing   *****************')
            print('***********************************************************')
            print('******************   NIEVES MATH GAME   *******************')
            print('***********************************************************')
            
        elif done == 1 and ops == 2:
            print('***********************************************************')
            print('***************   Lets Continue Playing   *****************')
            print('***********************************************************')
            print('******************   NIEVES MATH GAME   *******************')
            print('***********************************************************')
            
            
            print("*  Good Bye !!!                                           *")
            print('***********************************************************')
            print('*                  The Game is Over                       *')
            print('***********************************************************')
            exit()  
        elif done != 0 or 1 or 2: 
            print('Try again')
    except SystemError:
        
        print('something went wrong')


def level(level):
    difficulty = [1, 2, 3]
    for l in difficulty:
        if l == 1 and l == level:
            a = randint(0, 10)
            b = randint(0, 10)
            return a, b
        elif l == 2 and l == level:
            a = randint(0, 50)
            b = randint(0, 50)
            return a, b
        elif l == 3 and l == level:
            a = randint(0, 100)
            b = randint(0, 100)
            return a,b