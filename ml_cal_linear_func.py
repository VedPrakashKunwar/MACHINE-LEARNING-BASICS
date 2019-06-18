# import module
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sympy
from numpy.linalg import inv, det
x = np.linspace(0, 3, 301)
y = -1*(x**2) + 3*x - 1

plt.plot(x, y)
plt.show()

# limit
x,y = sympy.symbols('x y')
print(type(x))
y = x^2 + 1
print(y)

# f(x) = (-x2**2 +3*x2-1+1)/(x2-3)
#lim(x2-->2.9) (f(x2)-f(3))/(x2 - 3)
x2,y = sympy.symbols('x2 y')
limit_one = sympy.limit((-x2**2 +3*x2-1+1)/(x2-3) , x2, 2.9)

x = np.linspace(0, 50, 1000)
y1 = 30*x + 1000
y2 = 50*x + 100

plt.plot(x, y1, color='orange')
plt.plot(x, y2, color='blue')
plt.show()

matrix_one = np.asarray([
    [30, -1, -500],
    [50, -1, -100]  
], dtype=np.float32)

plt.axhline(0, c='black', lw=0.5)
plt.axvline(0, c='black', lw=0.5)
plt.xlim(-3,3)
plt.ylim(-4,4)

# Add your code here.
plt.quiver(0, 0, 2, 3, angles='xy', scale_units='xy', scale=1, color='blue')
plt.quiver(0, 0, -2, -3, angles='xy', scale_units='xy', scale=1, color='blue')
plt.quiver(0, 0, 1, 1, angles='xy', scale_units='xy', scale=1, color='gold')
plt.quiver(0, 0, 2, 2, angles='xy', scale_units='xy', scale=1, color='gold')
plt.show()

vector_one = np.asarray([
    [1],
    [2],
    [1]
], dtype=np.float32)

vector_two = np.asarray([
    [3],
    [0],
    [1]
], dtype=np.float32)

vector_linear_combination = 2*vector_one + 5*vector_two
dot_product = np.dot(vector_one[:, 0], vector_two)


w = np.asarray([
    [1]
    ,[2]
])
v = np.asarray([
    [3]
    ,[1]
])
end_point = 2*v - 2*w

matrix_a = np.asarray([
    [1.5, 3],
    [1, 4]
])


def matrix_inverse_two(mat):
    a = mat[0, 0]
    b = mat[0, 1]
    c = mat[1, 0]
    d = mat[1, 1]
    #det = 1/(a*d - b*c)
    try:
        det = 1/(a*d - b*c)
        mat_b = np.asarray([
                [d, -1*b]
                ,[-1*c, a]
                ])
        return det*mat_b
    except:
        print('Null Determinant')

# use inv function
inv_a_1 = matrix_inverse_two(matrix_a)
inv_a_2 = inv(matrix_a)
print(inv_a_1 == inv_a_2)
    

matrix_22 = np.asarray([
    [8, 4],
    [4, 2]
])

matrix_33 = np.asarray([
    [1, 1, 1],
    [1, 1, 6],
    [7, 8, 9]
])
det_22 = np.linalg.det(matrix_22)
det_33 = np.linalg.det(matrix_33)
    
    
    
    
    
    
    
    
    
    