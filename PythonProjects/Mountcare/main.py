class individual:
    def main(self, personal, one=0.0, two=0.0):
        self.personal = personal
        self.one = one
        self.two = two

        personaltot = personal * 0.15
        onetot = 0
        twotot = 0

        if one > 0:
            onetot = one * 0.05
            print(onetot)
        if two > 0:
            twotot = two * 0.03
            print(twotot)

        profit = personaltot + onetot + twotot
        return profit

    def pop(self):
        pass

    def push(self):
        pass

    def oneteam(self):
        return 0

    def twoteam(self):
        return 0


gopal = individual()  # direct from company
pravin = individual()  # gopal one
david = individual()  # gopal two

print(pravin.main(100000))
print(david.main(100000))
print(gopal.main(100000, gopal.oneteam(), gopal.twoteam()))
