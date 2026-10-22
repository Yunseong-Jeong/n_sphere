# N-sphere Convert to Spherical or Rectangular Coordination

import numpy as np
import torch

_VALID_TYPES = ('Tensor', 'ndarray', 'float', 'int', 'list')

def convert_spherical(input, digits= None):
    if(type(input).__name__ not in _VALID_TYPES):
        print("Input Error")
        return -1
    if digits is None:
        digits = 6 # Fixed Digits But if you want to change value, It can be helpful
    input_type = type(input).__name__
    result = _spherical_array(_to_float_array(input, input_type), digits)
    # A 1-D list comes back as a list, a 2-D (or larger) list as a numpy array
    return _wrap_result(result, input_type, list_max_ndim=1)

def convert_rectangular(input,digits=None):
    if(type(input).__name__ not in _VALID_TYPES):
        print("Input Error")
        return -1
    if digits is None:
        digits = 6
    input_type = type(input).__name__
    result = _rectangular_array(_to_float_array(input, input_type), digits)
    # A list always comes back as a (nested) list
    return _wrap_result(result, input_type, list_max_ndim=None)

def _to_float_array(input, input_type):
    # Tensor / ndarray / list -> float64 numpy array. The last axis holds one point,
    # every leading axis is a batch axis, so (n,), (m, n) and (b, m, n) all work.
    if(input_type == 'Tensor'):
        input = input.detach().cpu().numpy()
    array = np.asarray(input, dtype=np.float64)
    if(array.ndim < 1):
        raise ValueError("input must be a vector or an array of vectors, not a scalar")
    if(array.shape[-1] < 2):
        raise ValueError("every vector needs at least 2 values")
    return array

def _wrap_result(result, input_type, list_max_ndim):
    if(input_type == 'Tensor'):
        return torch.from_numpy(result)
    if(input_type == 'list' and (list_max_ndim is None or result.ndim <= list_max_ndim)):
        return result.tolist()
    return result

def _spherical_array(X, digits):
    # [x_1, ..., x_n] -> [r, Phi_1, ..., Phi_n-1] for every vector on the last axis.
    # Scaling by the largest |x| first keeps the squares from overflowing/underflowing.
    # The remaining radii are suffix norms sqrt(x_i^2 + ... + x_n^2) built from a
    # cumulative sum (no subtraction, so they never go negative through rounding),
    # and the angles use atan2, so there is no acos() domain error.
    scale = np.max(np.abs(X), axis=-1, keepdims=True)
    scale[scale == 0] = 1.0
    S = X / scale
    tail = np.sqrt(np.cumsum((S * S)[..., ::-1], axis=-1))[..., ::-1]  # tail[..., i] = sqrt(S_i^2 + ... + S_n^2)
    out = np.empty(X.shape, dtype=np.float64)
    out[..., 0] = tail[..., 0] * scale[..., 0]
    # Phi_i = acos(x_i / tail_i) written with atan2: always in [0, Pi]
    out[..., 1:-1] = np.round(np.arctan2(tail[..., 1:-1], S[..., :-2]), digits)
    # Last angle: the sign of x_n decides between [0, Pi] and (Pi, 2*Pi)
    last = np.arctan2(S[..., -1], S[..., -2])
    out[..., -1] = np.round(np.where(last < 0, last + 2 * np.pi, last), digits)
    return out

def _rectangular_array(P, digits):
    # [r, Phi_1, ..., Phi_n-1] -> [x_1, ..., x_n] for every vector on the last axis.
    r = P[..., :1]
    angle = P[..., 1:]
    # sin_prod[..., k] = sin(Phi_1) * ... * sin(Phi_k)  (1 for k = 0)
    sin_prod = np.ones(angle.shape, dtype=np.float64)
    sin_prod[..., 1:] = np.cumprod(np.sin(angle[..., :-1]), axis=-1)
    out = np.empty(P.shape, dtype=np.float64)
    out[..., :-1] = r * sin_prod * np.cos(angle)
    out[..., -1] = r[..., 0] * sin_prod[..., -1] * np.sin(angle[..., -1])
    return _round(out, digits)

def _round(array, digits):
    # np.round multiplies by 10**digits, which overflows for values near the float limit.
    # Such values have no fractional digits left to round, so they are kept as they are.
    with np.errstate(over='ignore', invalid='ignore'):
        rounded = np.round(array, digits)
    return np.where(np.isfinite(rounded), rounded, array)

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
