from teacher import Teacher
from student import Student
from alumni import Alumni
from person import Person


def main ():
    t = Teacher ('smith')
    s = Student ('jones')
    a = Alumni ('thompson')
    people = [Teacher(name = 'anderson'), Teacher(name = 'Su'), Student ('Ramirez'), Person('franco')]

    s.sleep()
    t.eat()
    a.eat()

    for p in people:
        p.introduction()
        p.sleep()
        p.eat()
        
        if type(p) is Teacher:
            p.teach()
        elif type(p) is Student:
            p.ask_question()


if __name__ == '__main__':
    main()



