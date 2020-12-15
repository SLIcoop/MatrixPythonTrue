#! /usr/bin/env python3

import numpy as np

i = 0
while i <= 2.1:
    x = np.random.random((4,4,4))
    y = np.random.random((4,4,4))
    R_MX = np.max(x)
    R_MN = np.min(x)
    L_MX = np.max(y)
    L_MN = np.min(y)
    print(x,"\n\n", y)

    #Find a large num in max
    if R_MX > L_MX:
        mx_First = R_MX
        mn_First = L_MX
    else:
        mx_First = L_MX
        mn_First = R_MX
    f = mx_First + mn_First
    
    #Find a small num in min
    if R_MN < L_MN:
        mx_Second = L_MN
        mn_Second = R_MN
    else:
        mx_Second = R_MN
        mn_Second = L_MN
    s = mx_Second + mn_Second

    i = f + s

print("\nThe largest number in the matrix: ", f)
print("\nThe smallest number in the matrix: ", s)
print(i)
