import numpy as np

## 1-D array
x = np.array([1, 2, 3])
print(x.ndim)

## 2-D array
Y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])
print(Y.ndim)

## Here the`zeros()` is an inbuilt function that you'll study on the next page. 
## The tuple (2, 3, 4( passed as an argument represents the shape of the ndarray
y = np.zeros((2, 3, 4))
print(y.ndim)

x = np.array([1, 2, 3, 4, 5])

## We print information about x
print('x = ', x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

## We create a rank 2 ndarray that only contains integers
Y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])

print('Y = \n', Y)

## We print information about Y
print('Y has dimensions:', Y.shape)
print('Y has a total of', Y.size, 'elements')
print('Y is an object of type:', type(Y))
print('The elements in Y are of type:', Y.dtype)

import numpy as np

# Replace None with appropriate code
X = np.arange(2,34,2).reshape(4,4)

### Notebook grading
solution = np.arange(2,34,2).reshape(4,4)

if type(X) != np.ndarray:
    print("`X` should be an ndarray")
elif np.array_equal(X, solution):
    print("Nice work! You can view my solution below")
elif X.shape != solution.shape:
    print("Your answer for `X` has a shape of {} but it should be 4 x 4".format(X.shape))
else:
    print("Your answer for `X` has the right shape but incorrect values")