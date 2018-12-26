def fiborabbit(n, k):
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n > 1:
        return fiborabbit(n-1, k) + k*fiborabbit(n-2, k)

print(fiborabbit(5, 3))



