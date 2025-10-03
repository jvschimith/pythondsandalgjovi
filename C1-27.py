def factors(n):
    results = []
    for i in range(1, n+1):
        if n % i == 0:
           yield i

factors_list = list(factors(12))
print(factors_list)  # Output: [1, 2, 3, 4, 6, 12]

