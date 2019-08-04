import numpy as np


def arrayParser(listString):
    """
    Parse the arrays passed into scripts using the input function.

    :param listString: comma or space delimited list of numbers
    :return: numpy array
    """
    if listString.find(',') == -1:
        return np.fromstring(listString, sep=' ')
    else:
        return np.fromstring(listString, sep=',')
