class Student():
    cname = "texas"
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name: ",self.name)
        print("Roll NO: ",self.roll)

    @classmethod
    def clzname(cls):
        print("Collage Name: ",cls.cname)

    @staticmethod
    def utilitymethod(x,y):
        print("Sum: ",x+y)


student1 = Student("ram",100)
student2 = Student("Sahil",200)


student1.display()
student1.clzname()
student2.display()
student2.clzname()
Student.utilitymethod(10,20)

