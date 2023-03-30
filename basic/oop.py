class Mobile:
    def __init__(self):
        print("ali hamza")


a = Mobile()


# constructor without parameter
class Mobile:
    def __init__(self):
        self.model = 'nokia'

    def show(self):
        print("model name:", self.model)


a = Mobile()
a.show()


# constructor with parameter

class Mobile:
    def __init__(self, n, m, v=80):
        self.name = n
        self.model = m
        self.volum = v

    def show(self, p):
        price = p  # local variabl

        print("name of mobile phone:", self.name)
        print("Model name:", self.model)
        print("volum", self.volum)
        print("price :", price)


# passing argument to the constructor
a = Mobile('nokia', '3310', 100)
# accessing method from outside class
a.show(1000)


