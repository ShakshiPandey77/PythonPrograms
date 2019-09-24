#Program 4 : University

class Student :
    def __init__(self):
        self.id =None
        self.age = None
        self.marks=None

    def validate_marks(self):
        marks = int(input("Enter marks :"))
        if marks<0 and marks > 100:
            return False
        else:
            self.set_marks(marks)
            return True

    def validate_age(self):
        age = int(input("Enter age:"))
        if age<=20:
            return False
        else:
            self.set_age(age)
            return True

    def set_marks(self,marks):
        self.marks = marks

    def set_age(self,age):
        self.age = age

    def set_id(self,id):
        self.id = id

    def get_marks(self):
        return self.marks

    def get_age(self):
        return self.age

    def get_id(self):
        return self.id

    def check_qualification(self):
        self.set_id(int(input("Enter id :")))
        if self.validate_age() and self.validate_marks():
            if self.marks >= 65 :
                return True
            else :
                return False
        else :
            print("Invalid data")
            return False
        
student1 = Student()
if student1.check_qualification():
    print("Qualified")
    print("ID :",student1.get_id())
    print("Age :",student1.get_age())
    print("Marks :",student1.get_marks())
else :
    print("Not qualified :(")
