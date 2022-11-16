from vector import Vector


def calculate(vectors: list):
    """
    Calculate the othogonal basis.

    :param vectors: a list of vector objects
    """

    # Setup the variables.
    newValue = []
    subtract = Vector([0] * len(vectors[0]))

    # Make Vector objects from the vectors given.
    for vector in range(len(vectors)):
        vectors[vector] = Vector(vectors[vector])

    # Check to see if they are already orthogonal.
    count = 0
    for i in range(len(vectors)):
        if Vector.isOrthogonal(vectors[i], vectors[i-1]):
            count += 1

    # If they are already orthogonal, return false.
    if count == len(vectors):
        return [x.value for x in vectors]

    # Perform the algorithm.
    for i in range(len(vectors)):
        newValue.append(vectors[i] + subtract)
        try:                        # Subtract until you cannot any more. Then, we are done.
            subtract -= (vectors[i+1].dotProduct(newValue[i]) /
                         newValue[i].dotProduct(newValue[i])) * newValue[i]
        except(IndexError):
            break

    # Return the result.
    return [[round(z, 3) for z in x.value] for x in newValue]
