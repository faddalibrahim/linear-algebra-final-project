class Vector:

    def __init__(self, v: list):

        self.value = v

    def dotProduct(self, other):

        return sum([x * y for x, y in zip(self.value, other.value)])

    def __add__(self, other):

        return Vector([x + y for x, y in zip(self.value, other.value)])

    def __sub__(self, other):

        return Vector([x - y for x, y in zip(self.value, other.value)])

    def __rmul__(self, scalar):

        return Vector([x * scalar for x in self.value])

    @staticmethod
    def isOrthogonal(vectorOne, vectorTwo):

        return vectorOne.dotProduct(vectorTwo) == 0

    def toString(self):

        return str(self.value)
