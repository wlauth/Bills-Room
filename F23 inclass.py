# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 13:07:58 2018
@author: ericw
"""
import sys

names = ('Amy', 'Ben', 'Cara')

#                  Function/Program
#                 +----------------+
#   INPUT  -->    |  PROCESSING    |  ---> OUTPUT
#                 +----------------+      function:return 
#

# REMEMBER:  Output of input() is str <string>

while(True):
    strIn = input('Please enter a number from 1 to 3: ')
    

    # Receive input5
    # Check the input

    try:
        num = int(strIn)
        print('Success: string converted to int:', num)
        if num > 0 and num <= 3:
            break
    except TypeError: 
        print('ERROR: Please ,enter an integer!')
        #sys.exit(1)
    except:
        print('ERROR: Bad input, program halted!')
        #sys.exit(1)
 
# More about the range() method/function...
#
#   THINKING ABOUT:   range(-1)
#
# range([start=0]), stop, [step=1]
#    
#example:   range(2) - - > 0, 1 
#
#           reange(2, 9) --> 2, 3, 4, 5, 6, 7, 8
#
#           range(2, 9, 3) -- > 2, 3, 4, 5, 6, 7, 8  [11 > 9 stop]
#
   
for iter in range(num):
    try:
        print('Hello, ', names[iter], '.', sep='')
    except IndexError:
        print('Please input an interger between 1~ 3 !')
        sys.exit(1)

    
    
    
    
    
    
    
    