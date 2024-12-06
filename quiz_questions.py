import random
import operator
from student import Student

class Question ():

    def __init__(self, maxvalue = 10, solution = 0, number = 1 ):
        self.number = 1
        self.maxvalue = 10 
        self.solution = 0
    

    def generateproblem(self, grade):
        """
        Generates an equation using random operator and numbers and prints the equation

        Parameters:
            none, returns solution to be used to check answer against input            
        """

   
        operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul), ('/', operator.truediv)]
        a= int(random.randrange(1,grade*10))   #problem is function of grade level so max value is based on student grade
        b = int(random.randrange(1,grade*10))
        op, equation = random.choice(operators)
        print (f'{a} {op} {b} =')
        self.solution = equation(a,b)
        f = open('Test_results.txt', 'a')
        f.write(f'Question:\n {a} {op} {b} = {self.solution}')
        f.close()
        # Equations.append(equationdetail)
        return self.solution
    