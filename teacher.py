from person import Person
class Teacher (Person):

    def __init__(self, name='', ID=-1, birthdate='1/1/2000'):
        Person.__init__(self,name, ID, birthdate)

    def teach(self):
        print(self.name + ' is teaching')

    def assign_homework(self, course):
        print(self.name + ' assigned homework for their ' + course + ' course.')

    def answer_question(self):
        print('Let me see if I can help')

    def introduction (self):
        print ('good morning, my name is professor ' + self.name)

    