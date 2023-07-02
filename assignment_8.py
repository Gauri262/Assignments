class A:
    def __init__(self):
        self.a = 10
        self._b = 20
        self.__c = 30

    def display(self):
        print("Values in Class A:")
        try:
            print("Private member c:", self.__c)
        except AttributeError:
            print("Error: Private member 'c' cannot be accessed.")

        print("Protected member b:", self._b)
        print("Public member a:", self.a)


class B(A):
    def display(self):
        print("Values in Class B:")
        print("Protected member b (inherited from Class A):", self._b)
        print("Public member a (inherited from Class A):", self.a)

obj = B()
obj.display()
