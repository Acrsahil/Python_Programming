class Student:
    def __init__(self, name, roll):
        print("hi")
        self.name = name
        self.roll = roll

    def display(self):
        print("hello")
        print("sahil is a god boy")
        print(self.name)
        print(self.roll)


student1 = Student("sahil", 23)
student2 = Student("hari", 28)
s = 0

Student.display(student1)
Student.display(student2)

print(student2.name)
