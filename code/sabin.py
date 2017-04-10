#!/usr/bin/python

# IMPORT OS OBJECT TO CLEAR SCREEN
import os
os.system("clear")

# DEFINE A DICTIONARY
fruits = {"apple":"bad","pear":"good"}   #  < this is the most phenomenal line of the whole script. It is the easiest way to use the functions of variables assignments and definitions.
print "What is a good fruit?"
# USE \n TO FORCE TO NEXT LINE NOT /n
choice = raw_input("Enter a good fruit.\n")
# CHECK IF CHOICE IS IN DICTIONARY
# USE .title TO CAPITALIZE FIRST LETTER OF STRING
# USE DICTIONARY ACCESSOR NOTATION DICT[key]
if choice in fruits:
    print choice.title() + "s are " + fruits[choice] + "!"
else:
    print choice.title() + " is not in my list of fruits!"
