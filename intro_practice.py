#this is a comment line

#importing packages
import pandas as pd
import numpy as np

#creatuing part
#creating variables
year = 2024 # a number variable
file_name = "HHA-506-practice" # a string variable
list_variable = [1,2,3,4,5] # a list
student_intro = {
    'name': 'zhaoyangliu',
    'age' : 27,
    'schools' : ['SBU', 'BJFU'],
    'adress' : {'city':'flushing' , 'state':'NY'}
} #a dictionary with a list and a nested dictionary

#creating a function
def function_final_grade(grade1,grade2):
    final_grade = 0.6 * grade1 + 0.4 * grade2
    if final_grade >=90:
        letter_grade = 'A'
    else:
         letter_grade = 'B'

    return final_grade, letter_grade

#printing part
print("number variable", year)
print("string variable", file_name)
print("list variable", list_variable)
print("dictionary variable", student_intro)

#function example
grade1 = 92
grade2 = 85
final_grade, letter_grade = function_final_grade(grade1,grade2)
print("Final Grade", final_grade)
print("Letter Grade", letter_grade)
