import string
from itertools import permutations
import random
import numpy as np

print("Enter the number of clauses ")
m = int(input())
print("Enter the number of variables in a clause ")
k = int(input())
print("Enter number of variables ")
n = int(input())
val = list(string.ascii_lowercase[:n])
for i in range(n):
    val.append(string.ascii_uppercase[i])
print(val)
options = list(permutations(val,k))
for i in range(5):
    res = list(np.zeros(m))
    for j in range(m):
        c = []
        literals = list(random.choice(options))
        print(literals)
        for p in range(k):
            c.append(literals[p] or literals[p+1])
        res[j] = c
print(res)