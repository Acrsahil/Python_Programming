class parent(object):
    def __init__(self):
        print("Parent class constructer")
    
    def display(self):
        print("i am the method from parent class")

    def property(self):
        print("Land+money")
    
class child(parent):

    def display(self): # ploypromism (changing parent function)
        print("I am bramacharya")


child1=child()
child1.property()
child1.display()