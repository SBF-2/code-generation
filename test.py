import numpy as np
a = np.random.rand(5,4)
print(a)
b = [i for i in range (a.shape[1]) if a[1,i] != 0]
print(b)