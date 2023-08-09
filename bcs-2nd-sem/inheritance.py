class parent(object):
    def __init__(self):
        print("Parent class constructer")
    
    def display(self):
        print("i am the method from parent class")
    
class child(parent):
    pass


child1=child()
child1.display()