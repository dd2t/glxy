def cross_multiplication(aux: float, min1: float, max1: float, min2: float,  max2: float) -> float:
    """ Similar to processing map.
        https://gist.github.com/companje/29408948f1e8be54dd5733a74ca49bb9
    """
    return min2 + (aux - min1) * (max2 - min2) / (max1 - min1)
