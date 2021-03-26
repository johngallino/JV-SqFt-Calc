# coding: utf-8 

import quotes
import random
import textwrap
import sys
from colorama import init, Fore, Back, Style

init(autoreset=True) #neccesary for colorama

floortotal= 0
htotal = 0
#print('random number from 0 to', len(quotes.quotes))
qnum = random.randint(0, (len(quotes.quotes)-1))

def isValid(num):  #checks if input is a valid float
    try:
        #print('num received is ', num)
        float(num)
        return(True)
    except:
        return(False)
    
def hasInches(num):  #checks if input contains both feet and inches
    if (' ' in str(num)):
        #print('input has inches')
        return True
    else:
        return False
    
def numParse(num): #parses input into feet and inches and returns total inches
    if hasInches(num):
            num = num.split(' ')
            #print ('num broken into ' + num[0] + ' and ' + num[1])
            if (isValid(num[0]) and isValid(num[1])):
                numInches = (float(num[0]) *12) + float(num[1])
                #print ('which is ' + str(numInches) + ' inches')
                return numInches
            else:
                return 0
    
    else: #if its just feet, check if its a number & turn it into inches anyway
        if (isValid(num) is True): #check if entered number is a number
            if (float(num) > 0): #check if number is positive
                #print('number is positive')
                numInches = float(num)*12
                #print('numinches returning ' + str(numInches))
                return numInches  
            elif(num == '-1' or num == -1): #check if number is -1
                return str(num)
            else: #if negative or 0
                return 0
                
            
        else: #num not a number
            return 0
        
def inchesToFeet(num):
    if ((num % 12) == 0):
        return (str(int(num/144)) + ' sq ft ')
    else:
        feet = num/144
        return ('about ' + str(int(feet)) + ' sq ft')
        

def oneRoom(floortotal, htotal):
    rl = input('Enter length: ').rstrip()
    
    if (rl == 'q'):
         sys.exit(0)
    elif (rl == '-1' or rl == -1):
        print('\n\t\t\tFloor total: ' + Fore.MAGENTA + Style.BRIGHT +  inchesToFeet(floortotal))
        htotal += floortotal
        repeat = input('Another floor? (y/n)')
        while (repeat != 'y' and repeat != 'n'):
                  repeat = input('Please input y or n: ')
        #print('repeat is ', repeat)
        if (repeat.lower() == 'n'):
            print('\n\t\t\tProperty Total: ' + Fore.YELLOW + Style.BRIGHT +  inchesToFeet(htotal))
            choice = input('\nDo another property? (y/n)')
            while (choice.lower() != 'y' and choice.lower() != 'n'):
                choice = input('Please input y or n: ')
            if (choice.lower() == 'y'):
                floortotal = 0
                htotal = 0
                print('\nStarting a new property...\n')
                oneRoom(floortotal, htotal)
            elif (choice.lower() == 'n'):
                print('Bye!')
                exit()
            else:
                print ('I can\'t believe you\'ve done this. You broke the program. Shame on you.')
        elif (repeat.lower() == 'y'):
            floortotal = 0
            oneRoom(floortotal, htotal)
        else:
            print ('I can\'t believe you\'ve done this. You broke the program. Shame on you.')
    else:
        rl = numParse(rl)
        while (float(rl) == 0):
            print (Fore.RED + Style.BRIGHT +'Invalid entry. Let\'s do that room again.')
            oneRoom(floortotal, htotal)
        #print('rl = %g in' % rl)
        rw = input('Enter width: ').rstrip()
        if (rw == 'q'):
            exit()
        else:
            rw = numParse(rw)
            while (float(rl) == 0):
                print (Fore.RED + Style.BRIGHT +'Invalid entry. Let\'s do that room again.')
                oneRoom(floortotal, htotal)
           
            rtotal = int(rl) * int(rw)
            print('\t\t\tRoom total: ' + Fore.GREEN + Style.BRIGHT + inchesToFeet(rtotal))
            floortotal += rtotal
            oneRoom(floortotal, htotal)
        
            
        
    
print('\nJUMPVISUAL SQ FOOTAGE CALCULATOR v2.2 for Mac')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#print('      created by john gallino')
print(Fore.CYAN + Style.BRIGHT + '\n' + textwrap.fill(quotes.quotes[qnum], 65) + '\n')
#choice = 'x'
#choice = input('Are you including inches in your measurements? (y/n): ')
#
#
#while (choice.lower() != 'y' and choice.lower() != 'n'):
#    choice = int(input('\nPlease enter y or n :'))
    

print('\nINSTRUCTIONS\n1. Starting with the first floor, enter the length and width of each room.\n2. If you are including inches, separate with a space. (e.g. \'8 3\' for 8ft 3in)\n3. Decimals work too. (e.g. \'10.5\' for 10ft 6in)\n4. When finished with a floor, enter \'-1\'\n')
oneRoom(floortotal, htotal)




    