# Bills-Room
ICS home work
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 12:49:56 2018

@author: User
"""

#@author: wlauth

# Stepps involved
# 0. Open the text file (for reading ~ the default)
# 0b Initialize dictionary
# 1. Read of process Line by Line
#for lineoftext in fhtext:
# fhtext ~ 'file handle to text file'
fname= 'passage.txt'

# Initialization dictionary

fhtext= open(fname)     # open('passage.txt')



words = {}   #words = dict()
for lineoftext in fhtext:
    # cleanup
    lineoftext = lineoftext.strip().replace('.','').replace(',','').replace(')','')
    lineoftext = lineoftext.replace('(',',').replace(')','').lower()
    # .split()into a list
    listwords = lineoftext.split()
    for aword in listwords:
        # use dictionary to count words
        #
        if aword in words.keys():
            # present, so increase the tally
            words[aword] += 1
        else:
            # not present, so "initialize" with value 1
            words[aword] = 1
        print(aword)
        
 #      print(listwords)
    #   print(lineoftext)
      
print(aword)
