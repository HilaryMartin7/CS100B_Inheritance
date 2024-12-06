from quiz_questions import Question
import emoji
import operator
from tabulate import tabulate

class Test:
    
    def __init__(self, questions = 1, numberIncorrect = 0):
        self.questions = questions
        self.numberIncorrect = int(numberIncorrect)    
 
    def presentQuestion(self,questionNumber, grade):

        q = Question(number = questionNumber)
        solution =Question.generateproblem(q, grade)
        answer = input('What is your answer?' )

        #check for format of answer and re-request if not digit
           
        while Test.is_number(answer) is False:
            answer = input('Invalid Answer. What is your answer?' )
        
        answer = float(answer)
           

        if Test.check_answer(answer, solution) is False:
            print (f'Sorry, That is incorrect.  The correct answer is {solution}')
            self.numberIncorrect += 1
            # answer = (input('That is incorrect.  Please try again. '))
            # while Test.is_number(answer) is False:
            #     answer = input('Invalid Answer. What is your answer?' )
        else: 
            print(emoji.emojize("That is correct. Great job! :thumbs_up:\n"))
        answer = float(answer)

        
        f = open('Test_results.txt', 'a')
        f.write(f'\n\tYour Answer:{answer}\n')
        f.close()
       

    def grade_test(self, questions):
        questions = int(questions)
        self.numberIncorrect = int(self.numberIncorrect)
        numberCorrect = questions - self.numberIncorrect
        grade = numberCorrect/questions
        f = open('Test_results.txt', 'a')
        f.write(f'\n\nYou had  {questions} and you missed {self.numberIncorrect}  \n Your final grade is {grade}\n' )
        f.close()

    
    def check_answer(answer, solution):
        """
        Generates an True value if the input is the correct answer

        Parameters:
            answer from input, returns true or false
        """
        answer = float(answer)
        
        if abs(answer - solution) < 0.1: 
            return True
        else: 
            return False

    def is_number(answer):
        """
        Checks a string to see if the input is numeric including negative or decimal

        Parameters:
            TRUE if numeric, FALSE if not
        """
        try:
            float(answer)
            return True
        except ValueError:
            return False 
        
