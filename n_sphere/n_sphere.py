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
        r = 0
        for i in range(0,len(input)):
            r += input[i]*input[i]
        r=math.sqrt(r)
        convert = [r]
        for i in range(0, len(input)-2):
            convert.append(round(math.acos(input[i]/r),digits))
            r=math.sqrt(r*r - input[i]*input[i])
        if(input[-2]>=0):
            convert.append(round(math.acos(input[-2]/r),digits))
        else:
            convert.append(round(2*math.pi - math.acos(input[-2]/r),digits))
        result = convert
        if(input_type=='ndarray'):
            result = np.array(result)
        elif(input_type== 'Tensor'):
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
        r = input[0]
        multi_sin = 1
        convert=[]
        if(input_type == 'Tensor'):
            for i in range(1, len(input)-1):
                convert.append(r* multi_sin * math.cos(input[i]))
                multi_sin *= math.sin(input[i])
            convert.append(r*multi_sin*math.cos(input[-1]))
            convert.append(r*multi_sin*math.sin(input[-1]))
            convert = np.array(convert)
            convert = torch.from_numpy(convert)
        else:
            for i in range(1, len(input)-1):
                convert.append(round(r* multi_sin * math.cos(input[i]),digits))
                multi_sin *= math.sin(input[i])
            convert.append(round(r*multi_sin*math.cos(input[-1]),digits))
            convert.append(round(r*multi_sin*math.sin(input[-1]),digits))
            if(input_type != 'list'):
                convert = np.array(convert)
        result = convert
    else:
        #over 2-dimension
        for element in range (0, len(input)):
            r = input[element][0]
            multi_sin = 1
            convert =[]
            if(input_type =='Tensor'):
                for i in range(1, len(input[element])-1):
                    convert.append(r * multi_sin * math.cos(input[element][i]))
                    multi_sin *= math.sin(input[element][i])
                convert.append(r*multi_sin*math.cos(input[element][-1]))
                convert.append(r*multi_sin*math.sin(input[element][-1]))
                convert = np.array(convert)
                convert = torch.from_numpy(convert)
                result +=[convert]
            else:
                for i in range(1, len(input[element])-1):
                    convert.append(round(r * multi_sin * math.cos(input[element][i]),digits))
                    multi_sin *= math.sin(input[element][i])
                convert.append(round(r*multi_sin*math.cos(input[element][-1]),digits))
                convert.append(round(r*multi_sin*math.sin(input[element][-1]),digits))
                if (input_type != 'list'):  # input == Numpy or Tensor
                    convert = np.array(convert)
                result +=[convert]
        if (input_type == 'ndarray'):
            result = np.array(result)
        elif (input_type == 'Tensor'):
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
