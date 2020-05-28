from operation import add, multi_add, subtraction
import os


def level():
    questions = int(input('How many questions to quiz? '))
    levels = int(input('Enter max digits or equation? '))
    return [questions,levels] 


def console():
    go = ('*' + ' ' * 28 + '   READY SET GO!!!!   ' + ' ' * 28 + '*')
    print('*' * 80)
    print('*' + ' ' * 28 + '   NIEVES MATH GAME   ' + ' ' * 28 + '*')
    print('*' * 80 + '\n')
    try:
        ops = int(input('''
        * Select your operation:

        * 1: for Addition
        * 2: for Multiple addition
        * 3: for Subtraction
        * 0: to  Exit
        
        \n        > '''))
    except ValueError:
        print('Please input one of the above options')
        input("Press any key to continue...")
        os.system('clear')
        console()
    
    if ops == 0:
        print('*' * 80)
        print('*' + ' ' * 28 +  '   The Game is Over   ' + ' ' * 28 + '*')
        print('*' + ' ' * 29 +  '     Good Bye !!!    '  + ' ' * 28 + '*')
        print('*' * 80)
        input('Press Enter to Continue...')
        os.system('clear')        
        exit()
    try:
        options = level()
        if ops == 1:
            os.system('clear')
            print('*' * 80)
            print(go)
            print('*' * 80,'\n')
            add(*options)
        elif ops == 2:
            os.system('clear')
            print('*' * 80)
            print(go)
            print('*' * 80,'\n')
            multi_add(*options)
        elif ops == 3:
            os.system('clear')
            print('*' * 80)
            print(go)
            print('*' * 80,'\n')
            subtraction(*options)
        else:
            print('* \n* Please enter a 1 for addition, 2 for subtraction.')
            console()    
    except ValueError:
        print('* \n* Please enter a number.')
    input("Press any key to continue...")
    os.system('clear')
    
    console()

