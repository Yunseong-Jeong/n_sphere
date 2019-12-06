# n_sphere

Spherical Coordinate system, Rectangular coordinate system and Stereographic Projection in N-sphere (Using Python)

https://pypi.org/project/n-sphere/

1. Spherical Coordinate ([Show Image](https://wikimedia.org/api/rest_v1/media/math/render/svg/fff301fb5050086e409e13519f82295f23b2987a))
    ```
    r = math.sqrt( (x_n)^2 + ((x_n-1)^2) + ... + (x_1)^2 )
    Phi_1 = math.acos( x_1 / math.sqrt((x_n)^2 + (x_n-1)^2 + ... + (x_1)^2 ))
    Phi_2 = math.acos( x_2 / math.sqrt((x_n)^2 + (x_n-1)^2 + ... + (x_2)^2 ))
    ...
    Phi_n-2 = math.acos( x_n-2 / math.sqrt((x_n)^2 + (x_n-1)^2 ))
    Phi_n-1 = math.acos( x_n-1 / math.sqrt((x_n)^2 + (x_n-1)^2 )) (x_n >= 0)
          = 2 * Pi - math.acos( x_n-1 / math.sqrt((x_n)^2 + (x_n-1)^2 )) (x_n < 0) 
    ```
   - R = radius
   - n - 1 angular coordinates Phi_1, Phi_2, ... , Phi_n-1  in n-dimensional Euclidean Space
   - Phi_1 , Phi_2 , ... , Phi_n-2 range over **[0, Pi]** radians
   - Phi_n-1 range over **[0, 2 * Pi)** radians
2. Rectangular Coordinate ([Show Image](https://wikimedia.org/api/rest_v1/media/math/render/svg/0c4349e9ce260f719ebf573067bc7b84305ae31c))
   ```
   x_1 = r * math.cos(Phi_1)
   x_2 = r * math.sin(Phi_1) * math.cos(Phi_2)
   x_3 = r * math.sin(Phi_1) * math.sin(Phi_2) * math.cos(Phi_3)
   ...
   x_n-1 = r * math.sin(Phi_1) * ... * math.sin(Phi_n-2) * math.cos(Phi_n-1)
   x_n = r * math.sin(Phi_1) * ... * math.sin(Phi_n-2) * math.sin(Phi_n-1)
   ``` 
   
3. Stereographic Projection (**incomplete**)
   - In 3-dimension
    ```
   [x,y,z] -> [x/1-z, y/1-z]
   ```
   - In N-dimension
   ```
   [x_1 , x_2 , ... , x_n] -> [ x_1 / 1-x_n , x_2 / 1-x_n , ... , x_n-1 / 1-x_n] 
   ```

4. Generating random points (Plan)


# Project Object
https://en.wikipedia.org/wiki/N-sphere

# How to Use
```
pip install n-sphere
```
- Tensor (Using Torch)
``` shell script
> python
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> import n_sphere
>>> x = torch.randint(10, size(5,3,))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'size' is not defined
>>> x = torch.randint(10, size=(5,3,))
>>> x
tensor([[1, 0, 4],
        [2, 7, 9],
        [1, 8, 6],
        [4, 9, 3],
        [0, 8, 1]])
>>> c_x = n_sphere.convert_spherical(x)
>>> c_x
tensor([[ 4.1231,  1.3258,  1.5708],
        [11.5758,  1.3972,  0.9098],
        [10.0499,  1.4711,  0.6435],
        [10.2956,  1.1718,  0.3218],
        [ 8.0623,  1.5708,  0.1244]], dtype=torch.float64)
>>> r_x = n_sphere.convert_rectangular(c_x)
>>> r_x
tensor([[1.0000e+00, 2.4493e-16, 4.0000e+00],
        [2.0000e+00, 7.0000e+00, 9.0000e+00],
        [1.0000e+00, 8.0000e+00, 6.0000e+00],
        [4.0000e+00, 9.0000e+00, 3.0000e+00],
        [2.6347e-06, 8.0000e+00, 1.0000e+00]], dtype=torch.float64)
```

- List
```shell script
>>> list = [
... [2,3,4,5,6],
... [4,1,3,6,7],
... [2,2,2,2,2],
... [4,9,1,2,8]]
>>> c_list = n_sphere.convert_spherical(list)
>>> c_list
array([[ 9.48683298,  1.358384  ,  1.241372  ,  1.097478  ,  0.87605805],
       [10.53565375,  1.181364  ,  1.468018  ,  1.256207  ,  0.86217005],
       [ 4.47213595,  1.107149  ,  1.047198  ,  0.955317  ,  0.78539816],
       [12.88409873,  1.255119  ,  0.745355  ,  1.450118  ,  1.32581766]])
>>> r_list = n_sphere.convert_rectangular(c_list)
>>> r_list
array([[2.000001, 3.      , 4.      , 5.      , 6.      ],
       [4.000001, 0.999996, 2.999996, 6.000001, 7.000001],
       [1.999999, 1.999999, 2.      , 2.000001, 2.000001],
       [4.000002, 9.000003, 0.999998, 1.999999, 7.999996]])
>>>
```
- Number of digits can be changed in Round Function (default = 6)

```sh
>>> list = [
... [2,3,4,5,6],
... [4,1,3,6,7],
... [2,2,2,2,2],
... [4,9,1,2,8]]
>>> c_list = n_sphere.convert_spherical(list,10)
>>> c_list
array([[ 9.48683298,  1.35838411,  1.24137205,  1.097478  ,  0.87605805],
       [10.53565375,  1.18136412,  1.46801764,  1.25620658,  0.86217005],
       [ 4.47213595,  1.10714872,  1.04719755,  0.95531662,  0.78539816],
       [12.88409873,  1.2551192 ,  0.74535537,  1.45011777,  1.32581766]])
>>> r_list = n_sphere.convert_rectangular(c_list,10)
>>> r_list
array([[2., 3., 4., 5., 6.],
       [4., 1., 3., 6., 7.],
       [2., 2., 2., 2., 2.],
       [4., 9., 1., 2., 8.]])
>>>
```

# Contact Us
yunseong14@naver.com

# Reference
- [N-sphere](https://en.wikipedia.org/wiki/N-sphere)
- [Stereographic projection](https://en.wikipedia.org/wiki/Stereographic_projection)

