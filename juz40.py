import numpy as np
from scipy.linalg import null_space 
A = np.array([[1,3],[9,7]])
v=np.array([2,3])
print(null_space(A))