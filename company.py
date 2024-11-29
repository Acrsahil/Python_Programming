class Person:
    name = "NULL"

    def __init__(self):
        self.name = ""
        self.address = ""
        self.phonenumber = ""
        self.id = ""

    def addname(self, name):
        self.name = name

    def addaddress(self, addr):
        self.address = addr

    def phone(self, phonenumber):
        self.phonenumber = phonenumber

    def Printdetails(self):
        print(f"Name -> {self.name}")
        print(f"Address -> {self.address}")
        print(f"Phone -> {self.phonenumber}")


p1 = Person()
p1.phone("98234134")
p1.addaddress("Ktm")
p1.addname("sahil")

p2 = Person()
p2.phone("2341243")
p2.addaddress("BTM")
p2.addname("Hari")



p2.Printdetails()
