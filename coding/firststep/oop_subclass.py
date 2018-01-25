# coding=UTF-8

class SchoolMember:
    '''代表任何学校里的人员'''

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('(Initialized schoolMember:{})'.format(self.name))

    def tell(self):
        '''告诉我有关我的细节'''
        print('Name:{},age:{}'.format(self.name,self.age))

class Teacher(SchoolMember):
    '''代表一位老师'''

    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print('(Initialized Teacher:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salray:{:d}'.format(self.salary))


class Student(SchoolMember):
    '''代表一位学生'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print('(Initialized Student:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:{:d}'.format(self.marks))


t = Teacher('Mrs.Chen',24,6000)
s = Student('chenpeng',23,10000)

print()

members = [t,s]
for member in members:
    member.tell()


