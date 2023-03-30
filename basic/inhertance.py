class A:
    def displayA(self):
        print("display A")


class B(A):
    def displayB(self):
        print("display B")


class C(B):
    def displayC(self):
        print("display C")


obj = C()
obj.displayA()
obj.displayB()
obj.displayC()
