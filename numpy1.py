import numpy as np

array_2d = np.random.randint(1, 101, size=(3, 3))
value = array_2d[1][0]
array_1d = np.arange(21, 41)
sliced = array_1d[1:8]

print("2D Array:\n", array_2d)
print("Size:", array_2d.size)
print("Dimensions:", array_2d.ndim)
print("Shape:", array_2d.shape)
print("Value at 2nd row, 1st column:", value)
print("Original 1D Array:", array_1d)
print("Sliced (2nd to 8th element):", sliced)