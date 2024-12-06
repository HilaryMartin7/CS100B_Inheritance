import random
import operator
from student import Student

class Question ():

    def __init__(self, maxvalue = 10, solution = 0, number = 1 ):
        self.number = 1
        self.maxvalue = 10 
        self.solution = 0
    
    def grade_level(self,grade):
        if grade > 9: 
            maxvalue == int(1000)
        elif grade > 6:
            maxvalue == int(100)
        elif grade > 3:
            self.maxvalue == int(50)
        else:
            maxvalue == int(10)
        return maxvalue
       


    def generateproblem(self, grade):
        """
        Generates an equation using random operator and numbers and prints the equation

        Parameters:
            none, returns solution to be used to check answer against input            
        """

        if grade > 9: 
            self.maxvalue == int(1000)
        elif grade > 6:
            self.maxvalue == int(100)
        elif grade > 3:
            self.maxvalue == int(50)
        else:
            self.maxvalue == int(10)
   
        operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul), ('/', operator.truediv)]
        a= int(random.randrange(1,self.maxvalue))
        b = int(random.randrange(1,self.maxvalue))
        op, equation = random.choice(operators)
        print (f'{a} {op} {b} =')
        self.solution = equation(a,b)
        # Equations.append(equationdetail)
        return self.solution
    