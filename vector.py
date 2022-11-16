class Vector:
    """
    A helper class. Offers dot product multiplication
    as well as standard multiplication.
    """

    def __init__(self, v: list):
        """
        Constructor for the Vector class.

        :param v: the vector values.
        """

        self.value = v

    def dotProduct(self, other):
        """
        Performs a dot product operation
        with another vector. 

        :param other: the other vector.
        :return: the resulting vector.
        """

        return sum([x * y for x, y in zip(self.value, other.value)])

    def __add__(self, other):
        """
        Performs a standard vector-vector
        addition. 

        :param other: the other vector.
        :return: the resulting vector.
        """

        return Vector([x + y for x, y in zip(self.value, other.value)])

    def __sub__(self, other):
        """
        Allows you to subtract vectors.

        :param other: the other vector.
        :return: the resulting vector.
        """

        return Vector([x - y for x, y in zip(self.value, other.value)])

    def __rmul__(self, scalar):
        """
        Performs a standard vector-scalar 
        multiplication. Overrides the 
        standard multiplication.

        :param scalar: the scalar to multiply by.
        :return: the resulting vector.
        """

        return Vector([x * scalar for x in self.value])

    @staticmethod
    def isOrthogonal(vectorOne, vectorTwo):
        """
        Checks to see if two vectors multiply
        to equal zero. If they do, then they're
        orthogonal.

        :param vectorOne: The first vector.
        :param vectorTwo: The second vector.
        :return: True if the vectors are orthogonal.
        """

        return vectorOne.dotProduct(vectorTwo) == 0

    def toString(self):
        """
        Allows us to easily view the contents of 
        the vector.

        :return: a string representation of the vector.
        """

        return str(self.value)
