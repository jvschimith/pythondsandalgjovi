
def norm_of_vector(a):
    """Calculate the norm of a vector."""
    for i in range(len(a)):
        a[i] = float(a[i])
    norm = 0
    for i in range(len(a)):
        norm += a[i] ** 2
    return norm ** 0.5

aa = input("Enter a vector of numbers separated by commas: ").split(',')
print(norm_of_vector(aa))
