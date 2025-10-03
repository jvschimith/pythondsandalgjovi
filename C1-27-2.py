def gerador_numeros():
    for i in range(5):
        yield i  # atribui um valor a i e retorna
    yield 5  # Retorna o último valor

# Uso:
gen = gerador_numeros()
for num in gen:
    print(num)