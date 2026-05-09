from numba import cuda
import numpy as np


@cuda.jit
def vector_add(a,b,c):

  i = cuda.threadIdx.x

  c[i] = a[i] + b[i]

a = np.array([1,2,3,4,5,6])
b = np.array([6,5,4,3,2,1])
c = np.zeros(6)

vector_add[1,6](a,b,c)
print("vector addition : ")
print(c)

@cuda.jit
def vector_multi(a,b,c):
  row , col =cuda.grid(2)
  if row < c.shape[0] and col < c.shape[1]:
    c[row][col]=0
    for k in range(a.shape[1]):
      c[row][col] += a[row][k] * b[k][col]

a=np.array([[1,2],[3,4]])
b= np.array([[5,6],[7,8]])
c= np.zeros((2,2))
vector_multi[(1,1),(2,2)](a,b,c)
print("Matrix Multiplication:")

print(c)
