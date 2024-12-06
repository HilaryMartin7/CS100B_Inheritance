from quiz_questions import Question
import emoji
import operator

class Test:
    
    def __init__(self, questions = 1 ):
        self.questions = questions

    def presentQuestion(questionNumber, grade):

        q = Question(number = questionNumber)
        solution =Question.generateproblem(q, grade)
        answer = input('What is your answer?' )

        #check for format of answer and re-request if not digit

            
        while Test.is_number(answer) is False:
            answer = input('Invalid Answer. What is your answer?' )
        answer = float(answer)



            #If answer is digit, convert to int to compare since a and b are int 
            #If not correct request input again, check that for numeric before comparing to solution
            #answer = int(answer)

        while Test.check_answer(answer, solution) is False:
            answer = (input('That is incorrect.  Please try again. '))
            while Test.is_number(answer) is False:
                answer = input('Invalid Answer. What is your answer?' )

        answer = float(answer)

        print(emoji.emojize("That is correct. Great job! :thumbs_up:\n"))


    
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