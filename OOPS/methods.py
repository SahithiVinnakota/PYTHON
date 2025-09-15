class Student:

    #class variable
    school= 'Sri Chaithanya'

    def __init__(self,m1,m2,m3):

        #instance variables

        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    #class Method
    @classmethod
    def getSchool(cls):
        return cls.school
    
    #static Method
    @staticmethod    
    def info():
        print("this is student class")

    #instance methods
    
    # def get_m1(self):       #getters fetch the value
    #     return self.m1
    
    # def set_m1(self,value): #setters modify the value
    #     self.m1=value
    
    
s1=Student(23,46,32)
s2=Student(33,45,21)

#print(s1.avg())
#print(Student.getSchool)

Student.info()