import numpy as np # nubpy / list 차이는 속도 차이가 많이 난다. numpy는 c언어로 만들어져서 빠르다. list는 python으로 만들어져서 느리다.

arr = np.array([1, 2, 3, 4, 5])
print(type(arr))
print(arr)

arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

print(arr2)