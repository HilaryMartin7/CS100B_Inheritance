import emoji
import random
import operator
from student import Student 
from test import Test
from quiz_questions import Question

#ask user for name
studentname = input('What is your name? ')

s= Student (name = studentname)
s.welcome()


#Allow user to set number of questions
numberOfQuestions = (input('How many questions would you like? '))

#Make sure the user enters a positive digit
while numberOfQuestions.isdigit() == False:
    print ("please enter a valid number")
    numberOfQuestions = (input('How many questions would you like? '))

t = Test(questions = numberOfQuestions)
numberOfQuestions = int(numberOfQuestions)

gradelevel = (input('What grade are you in? '))

#Make sure the user enters a positive digit
while gradelevel.isdigit() == False:
    print ("please enter a valid grade")
    gradelevel = (input('What grade are you in? '))
questionNumber = int(1)
s.grade = int(gradelevel)
# q = Question.grade_level(questionNumber, s.grade)




#define variable for Question number to loop from 1-10

#print (questionNumber)
#found the module operator with add, sub mul functions
#use the operator to define the string used to display as well as the function to calculate

#list to store equations as they are generated to report back to user at end
# Equations= []
# #adding header row to test tabular display
# headers = ("value", "op", "value2", "solution", "answer")
# Equations.append(headers)


 


#Show the function to the user and prompt for answer

while questionNumber <= numberOfQuestions:
    t= Test.presentQuestion(questionNumber, s.grade)
    questionNumber = questionNumber + 1


#since the tuple that stores the equation and answer are generated in the function
#prior to user answer being entered, this replaces the placeholder value in the tuple
#with the user value using a temp list method. 
#     temp_list = list(Equations[-1])  # Access the last element (tuple) and convert to list
#     temp_list[4] = answer  # Change the second element of the tuple
#     Equations[-1] = tuple(temp_list)  # Replace the tuple in the list
#     questionNumber = questionNumber + 1


# from tabulate import tabulate
# table = tabulate (Equations)
# print(table)