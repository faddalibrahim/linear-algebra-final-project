from vector import Vector


def calculate(vectors: list):
    """
    Calculating the Orthogonal Basis.

    :param vectors: a list of vector objects
    """

    newValue = []
    subtract = Vector([0] * len(vectors[0]))

    for vector in range(len(vectors)):
        vectors[vector] = Vector(vectors[vector])

    count = 0
    for i in range(len(vectors)):
        if Vector.isOrthogonal(vectors[i], vectors[i-1]):
            count += 1

    if count == len(vectors):
        return [x.value for x in vectors]

    for i in range(len(vectors)):
        newValue.append(vectors[i] + subtract)
        try:
            subtract -= (vectors[i+1].dotProduct(newValue[i]) /
                         newValue[i].dotProduct(newValue[i])) * newValue[i]
        except(IndexError):
            break

    return [[round(z, 3) for z in x.value] for x in newValue]
