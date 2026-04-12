# LEARNING Goal: Module imports, aliases, and function reuse
# This script shows how to import functions and variables from another Python module.
# It teaches: module imports, how to call imported functions, and how imported values are used.

from my_module import find_index, test
import sys
#import my_module as mm #The as argument is short for alias

courses = ['History','Math','Physics','CompSci']

index = find_index(courses,'Math')
print(index)
print (test)
