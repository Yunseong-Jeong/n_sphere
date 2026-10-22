# N-sphere Convert to Spherical or Rectangular Coordination

import numpy as np
import math
import torch

def convert_spherical(input, digits= None):
    if(not(
            type(input).__name__ == 'Tensor'
        or  type(input).__name__ == 'ndarray'
        or  type(input).__name__ == 'float'
        or  type(input).__name__ == 'int'
        or  type(input).__name__ == 'list'
    )):
        print("Input Error")
        return -1
    # Check Numpy or list
    if digits is None:
        digits = 6 # Fixed Digits But if you want to change value, It can be helpful
    result =[]
    input_type = type(input).__name__
    if(input_type == 'list'):
        input = np.array(input)
    #over 2-dimension (current available 2-dimension)
    if(input.ndim==1):
        result = _spherical_of_vector(input, digits)
        if(input_type=='ndarray'):
            result = np.array(result)
        elif(input_type== 'Tensor'):
            result = torch.tensor(result, dtype=torch.float64)
    else:
        for element in range(0, len(input)):
            convert = _spherical_of_vector(input[element], digits)
            if(type(input[element]).__name__ != 'list'): #input == Numpy or Tensor
                convert = np.array(convert)
                if(type(input[element]).__name__ == 'Tensor'):
                    convert = torch.from_numpy(convert)
            result += [convert]
        if(type(input).__name__ == 'ndarray'):
            result = np.array(result)
        elif(type(input).__name__=='Tensor'):
            result = torch.stack(result)
    return result

def _spherical_of_vector(vector, digits):
    # Convert one rectangular vector [x_1, ..., x_n] to [r, Phi_1, ..., Phi_n-1].
    # The remaining radius is never obtained by subtracting squares (that can go
    # slightly negative or push acos() outside [-1, 1] through rounding error);
    # the suffix norms sqrt(x_i^2 + ... + x_n^2) are accumulated with hypot instead.
    values = [float(v) for v in vector]
    n = len(values)
    if(n < 2):
        raise ValueError("convert_spherical needs at least 2 dimensions")
    tail = [0.0] * (n + 1)  # tail[i] = sqrt(x_i^2 + ... + x_n^2), tail[n] = 0
    for i in range(n - 1, -1, -1):
        tail[i] = math.hypot(tail[i + 1], values[i])
    convert = [tail[0]]
    for i in range(0, n - 2):
        # Phi_i = acos(x_i / tail[i]) written with atan2: always in [0, Pi], no domain error
        convert.append(round(math.atan2(tail[i + 1], values[i]), digits))
    # Last angle: the sign of x_n (values[-1]) decides between [0, Pi] and (Pi, 2*Pi)
    last = math.atan2(values[-1], values[-2])
    if(last < 0):
        last += 2 * math.pi
    convert.append(round(last, digits))
    return convert

def convert_rectangular(input,digits=None):
    if (not (
            type(input).__name__ == 'Tensor'
            or type(input).__name__ == 'ndarray'
            or type(input).__name__ == 'float'
            or type(input).__name__ == 'int'
            or type(input).__name__ == 'list'
    )):
        print("Input Error")
        return -1
    # Check Numpy or list
    if digits is None:
        digits = 6
    result = []
    input_type = type(input).__name__
    if(input_type=='list'):
        input = np.array(input)
    if(input.ndim==1):
        result = _rectangular_of_vector(input, digits)
        if(input_type == 'ndarray'):
            result = np.array(result)
        elif(input_type == 'Tensor'):
            result = torch.tensor(result, dtype=torch.float64)
    else:
        #over 2-dimension
        for element in range (0, len(input)):
            convert = _rectangular_of_vector(input[element], digits)
            if (input_type != 'list'):  # input == Numpy or Tensor
                convert = np.array(convert)
                if(input_type == 'Tensor'):
                    convert = torch.from_numpy(convert)
            result +=[convert]
        if (input_type == 'ndarray'):
            result = np.array(result)
        elif (input_type == 'Tensor'):
            result = torch.stack(result)
    return result

def _rectangular_of_vector(vector, digits):
    # Convert one spherical vector [r, Phi_1, ..., Phi_n-1] to [x_1, ..., x_n].
    # Plain floats are used so that `digits` rounding also works for Tensor input.
    values = [float(v) for v in vector]
    if(len(values) < 2):
        raise ValueError("convert_rectangular needs at least 2 values (r and one angle)")
    r = values[0]
    multi_sin = 1.0
    convert = []
    for i in range(1, len(values)-1):
        convert.append(round(r * multi_sin * math.cos(values[i]), digits))
        multi_sin *= math.sin(values[i])
    convert.append(round(r*multi_sin*math.cos(values[-1]), digits))
    convert.append(round(r*multi_sin*math.sin(values[-1]), digits))
    return convert

#### Temporary Not Use
def Stereographic_Projection(input, digits=None):
    if digits is None:
        digits = 6; # Fixed Digits But if you want to change value, It can be helpful
    ischeck = False
    if(type(input).__name__ != 'list'):
        if (input.ndim > 1):
            input = input.flatten()
        input = input.tolist()
        ischeck =True
    last_index = input[-1];
    numpy_length = len(input)
    result = []
    for i in range(0, numpy_length-1):
        result.append(round((input[i] / (1-last_index)),digits))
    if(ischeck):
        result = np.array(result)
    return result
