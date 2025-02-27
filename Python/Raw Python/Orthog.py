# orthog - Program to test if a pair of vectors 
# is orthogonal.  Assumes vectors are in 3D space

# Set up configuration options and special features
import numpy as np
from nm4p.input_parser import arrayParser

#* Initialize the vectors a and b
a = arrayParser(input('Enter the first vector without square brackets: '))
b = arrayParser(input('Enter the second vector without square brackets: '))

#* Evaluate the dot product as sum over products of elements
a_dot_b = 0.
for i in range(3):
    a_dot_b += a[i] * b[i]

#* Print dot product and state whether vectors are orthogonal
if a_dot_b == 0:
    print('Vectors are orthogonal')
else:
    print('Vectors are NOT orthogonal')
    print('Dot product = ' , a_dot_b)

