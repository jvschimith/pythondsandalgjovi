a = input().split()
b = 2

def mutable(a, b):
    for i in range(len(a)):
        a[i] *= b
    return a

a = list(map(int, a))  # Convert input strings to integers
print(mutable(a, b))