def seq():
    n = 0
    num = 0
    while True:
        yield num
        n += 2
        num += n

# Gera sequencia de 0 a 90, pulando de n+2
gen = seq()
for i in range(10):
    print(next(gen), end='  ')