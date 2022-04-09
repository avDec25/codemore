import functools

a = [1, 2, 3, 2, 1, 4, 4, 5]
jt = 1
i = 0
n = len(a)

vindi = []

if jt == 1:
    for j in range(i+1, n):
        if a[i] <= a[j]:
            vindi.append(j)
