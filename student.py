from person import Person
class Student:

    def __init__(self, name='', ID=-1, birthdate='1/1/2000', grade= 1):
        self.name = name
        self.ID = ID
        self.birthdate = birthdate
        self.grade = grade

    def grade_level(self):
        if self.grade > 9: 
            self.maxvalue == 1000
        elif self.grade > 6:
            self.maxvalue == 100
        elif self.grade > 3:
            self.maxvalue == 50
        else:
            self.maxvalue == 10
        return self.maxvalue


    def study(self):
        print(self.name + ' is studying')

    def do_homework(self, course):
        print(self.name + ' is doing homework for their ' + course + ' course.')

    def ask_question(self):
        print('Wait, what?')
    
    def introduction(self):
        print ('yo my name is ' + self.name)

    def welcome(self):
        print ('Welcome ' + self.name + '! Let''s take a math quiz!')

