# N-sphere Convert to Spherical or Rectangular Coordination

import numpy as np
import math

def convert_spherical(input):
    # Check Numpy or list
    ischeck = False
    if(type(input).__name__ != 'list'):
        if (input.ndim > 1):
            input = input.flatten
        input = input.tolist()
        ischeck =True
    r = 0
    for i in range(0, len(input)):
        r += input[i]*input[i]
    r = math.sqrt(r);
    result = [r]
    for i in range (0 ,len(input)-2):
        result.append(math.acos(input[i] / r))
        r = math.sqrt(r*r - input[i]*input[i])
    if(input[-2] >= 0):
        result.append(math.acos(input[-2]/r))
    else:
        result.append(2*math.pi - math.acos(input[-2] /r))

    print(result)
    if(ischeck): #input == Numpy
        result = np.array(result)
    return result

def convert_rectangular(input):
    # Check Numpy or list
    ischeck = False
    if (type(input).__name__ != 'list'):
        if (input.ndim > 1):
            input = input.flatten
        input = input.tolist()
        ischeck = True
    numpy_length = len(input)
    r = input[0]
    multi_sin = 1
    result =[]
    for i in range(1, numpy_length-1):
        result.append(r*multi_sin*math.cos(input[i]))
        multi_sin *= math.sin(input[i])
    result.append(r*multi_sin*math.cos(input[-1]))
    result.append(r*multi_sin*math.sin(input[-1]))
    return result

list = [3,4,5]
test = np.array(list)
print(test)
test = convert_spherical(test)
print(test)
test = convert_rectangular(test)
print(test)
