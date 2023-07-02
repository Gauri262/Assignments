class A:
    def __init__(self, a, b, c):
        self.a = b
        self._b = b
        self.__c = c

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

obj = B(10, 20, 30)
obj.display()
