def dotproduct(a, b):
    map(int, a)
    map(int, b)
    prod = 0    
    # return sum(a[i] * b[i] for i in range(len(a)))
    for i in range(len(a)):
        prod += a[i] * b[i]
    return prod

a = [1, -8, 3]
b = [4, 5, 4]
print(dotproduct(a, b))