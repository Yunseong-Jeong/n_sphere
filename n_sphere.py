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
    )):
        print("Input Error")
        return -1

    # Check Numpy or list
    if digits is None:
        digits = 6 # Fixed Digits But if you want to change value, It can be helpful
    result =[]
    dimension=[]
    pointer = input
    while(True):
        if(len(pointer)):
            dimension.append(len(pointer))
            pointer = pointer[0]
        else:
            break
    #over 2-dimension (current available 2-dimension)
    if(len(dimension)==1):
        r = 0
        for i in range(0,dimension[0]):
            r += input[i]*input[i]
        r=math.sqrt(r)
        convert = [r]
        for i in range(0, dimension[0]-2):
            convert.append(round(math.acos(input[i]/r),digits))
            r=math.sqrt(r*r - input[i]*input[i])
        if(input[-2]>=0):
            convert.append(math.acos(input[-2]/r))
        else:
            convert.append(2*math.pi - math.acos(input[-2]/r))
        if(type(input).__name__!= 'list'):
            convert = np.array(convert)
            if(type(input).__name__=='Tensor'):
                convert = torch.from_numpy(convert)
        result += [convert]
        if(type(input).__name__=='ndarray'):
            result = np.array(result)
        elif(type(input).__name__ == 'Tensor'):
            result = torch.stack(result)
    else:
        for element in range(0, len(input)):
            r = 0
            for i in range(0, len(input[element])):
                r += input[element][i]*input[element][i]
            r = math.sqrt(r)
            convert = [r]
            for i in range (0 ,len(input[element])-2):
                convert.append(round(math.acos(input[element][i] / r),digits))
                r = math.sqrt(r*r - input[element][i]*input[element][i])
            if(input[element][-2] >= 0):
                convert.append(math.acos(input[element][-2]/r))
            else:
                convert.append(2*math.pi - math.acos(input[element][-2] /r))
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

def convert_rectangular(input,digits=None):
    if (not (
            type(input).__name__ == 'Tensor'
            or type(input).__name__ == 'ndarray'
            or type(input).__name__ == 'float'
            or type(input).__name__ == 'int'
    )):
        print("Input Error")
        return -1
    # Check Numpy or list
    if digits is None:
        digits = 6
    result = []
    #over 2-dimension
    for element in range (0, len(input)):
        r = input[element][0]
        multi_sin = 1
        convert =[]
        for i in range(1, len(input[element])-1):
            #convert.append(round(r*multi_sin*math.cos(input[element][i]),digits))
            convert.append(r * multi_sin * math.cos(input[element][i]))
            multi_sin *= math.sin(input[element][i])
        #convert.append(round(r*multi_sin*math.cos(input[element][-1]),digits))
        #convert.append(round(r*multi_sin*math.sin(input[element][-1]),digits))
        convert.append(r*multi_sin*math.cos(input[element][-1]))
        convert.append(r*multi_sin*math.sin(input[element][-1]))
        if (type(input).__name__ != 'list'):  # input == Numpy or Tensor
            convert = np.array(convert)
            if (type(input).__name__ == 'Tensor'):
                convert = torch.from_numpy(convert)
        print(convert)
        result +=[convert]
        print(result)
    if (type(input).__name__ == 'ndarray'):
        result = np.array(result)
    elif (type(input).__name__ == 'Tensor'):
        result = torch.stack(result)
    return result

#### Temporary Not Use
def Stereographic_Projection(input, digits=None):
    last_index = input[-1];
    if digits is None:
        digits = 6; # Fixed Digits But if you want to change value, It can be helpful
    ischeck = False
    if(type(input).__name__ != 'list'):
        if (input.ndim > 1):
            input = input.flatten
        input = input.tolist()
        ischeck =True
    numpy_length = len(input)
    result = []
    for i in range(0, numpy_length-1):
        result.append(round((input[i] / (1-last_index)),digits))
    if(ischeck):
        result = np.array(result)
    return result
