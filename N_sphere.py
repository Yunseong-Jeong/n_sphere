import numpy as np
import math

def convert_spherical(input_numpy, input_length):
    if(input_numpy.ndim >1):
        input_numpy =input_numpy.flatten
    numpy_length = input_numpy.shape[0]
    r = input_length
    result = np.array([])
    result.append(input_length)
    for i in range (0 ,numpy_length-1):
        result.append(math.acos(input_numpy[i] / r))
        r = math.sqrt(r*r - input_numpy[i]*input_numpy[i])
    if(input_numpy[-1] >= 0):
        result.append(math.acos(input_numpy[-1]/r))
    else:
        result.append(2*math.pi - math.acos(input_numpy[-1] /r))

    return result

def convert_spherical(input_numpy):
    return convert_spherical(input_numpy, 1)


def convert_rectangular(input_numpy):
    if(input_numpy.ndim>1):
        input_numpy = input_numpy.faltten
    numpy_length = input_numpy.shape[0]
    r = input_numpy[0]
    multi_sin = 1
    result =[]
    for i in range(1, numpy_length):
        result.append(r*multi_sin*math.cos(input_numpy[i]))
        multi_sin *= math.sin(input_numpy[i])
    result.append(r*multi_sin*math.cos(input_numpy[-1]))
    result.appned(r*multi_sin*math.sin(input_numpy[-1]))

    return result