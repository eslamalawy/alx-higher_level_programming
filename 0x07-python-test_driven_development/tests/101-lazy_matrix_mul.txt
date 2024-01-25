>>> matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

>>> print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
[[ 7 10]
 [15 22]]

>>> print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
[[13 16]]

>>> print(matrix_mul([[1, 2.3], [3.4, 4.2]], [[1.3, 2.3], [3.3, 4.1]]))
[[ 8.89 11.73]
 [18.28 25.04]]

>>> print(matrix_mul([[1.0, 2.0], [3.0, 4.0]], [[1.0, 2], [3, 4]]))
[[ 7. 10.]
 [15. 22.]]

"""
Error
"""

>>> try:
...	print(matrix_mul([[1, 2, 3]], [1, 2, 3]))
... except Exception as te:
...	print(te)
[14]

>>> try:
...	print(matrix_mul([[1, "HELLO"]], [[3, 4], [5, 6]]))
... except Exception as te:
... 	print(te)
invalid data type for einsum

>>> try:
...	print(matrix_mul([[1, 2], [3, 4]], [[1, 2], ["3", 4]]))
... except Exception as te:
... 	print(te)
invalid data type for einsum


>>> try:
...	print(matrix_mul([[1], [2]], [[3, 4], [5, 6]]))
... except Exception as te:
... 	print(te)
shapes (2,1) and (2,2) not aligned: 1 (dim 1) != 2 (dim 0)


>>> try:
...	print(matrix_mul([[1], [3, 2]], [[3, 4], [5, 6]]))
... except Exception as te:
... 	print(te)
setting an array element with a sequence.

>>> try:
...	print(matrix_mul([[1], [2]], [[2, 3, 4], [5, 6]]))
... except Exception as te:
... 	print(te)
setting an array element with a sequence.

>>> try:
...	print(matrix_mul(None, None))
... except Exception as te:
... 	print(te)
Object arrays are not currently supported

>>> try:
...	print(matrix_mul([1, 2], None))
... except Exception as te:
... 	print(te)
Object arrays are not currently supported

>>> try:
...	print(matrix_mul([], []))
... except Exception as te:
... 	print(te)
0.0

>>> try:
...	print(matrix_mul([None], []))
... except Exception as te:
... 	print(te)
Object arrays are not currently supported

>>> try:
...	print(matrix_mul([1, 2, 3], []))
... except Exception as te:
... 	print(te)
shapes (3,) and (0,) not aligned: 3 (dim 0) != 0 (dim 0)

>>> try:
...	print(matrix_mul([1, 2, 3], [None]))
... except Exception as te:
... 	print(te)
Object arrays are not currently supported

>>> try:
...	print(matrix_mul([[1, 2, 3]], [None]))
... except Exception as te:
... 	print(te)
Object arrays are not currently supported

>>> try:
...	print(matrix_mul([[5, 6], [7, 8]], [[]]))
... except Exception as te:
... 	print(te)
shapes (2,2) and (1,0) not aligned: 2 (dim 1) != 1 (dim 0)

>>> try:
...	print(matrix_mul([[1, 2], [3, 4], [3, 4]], [[5, 6, 1], [7, 8, 2]]))
... except Exception as te:
... 	print(te)
[[19 22  5]
 [43 50 11]
 [43 50 11]]

>>> try:
...	print(matrix_mul([[1, 2, 3]], ))
... except Exception as te:
...	print(te)
lazy_matrix_mul() missing 1 required positional argument: 'm_b'

>>> try:
...	print(matrix_mul())
... except Exception as te:
...	print(te)
lazy_matrix_mul() missing 2 required positional arguments: 'm_a' and 'm_b'
