def quadrados_lista(n):
    result = []  # Armazena todos os resultados em uma lista
    for i in range(n):
        result.append(i ** 2)
    return result  # Retorna a lista completa

# Uso:
numeros_quadrados = quadrados_lista(5)
print(numeros_quadrados)  # Saída: [0, 1, 4, 9, 16]

def quadrados_gerador(n):
    for i in range(n):
        yield i ** 2  # Produz um valor por vez (lazy evaluation)

# Uso:
gerador_quadrados = quadrados_gerador(5)
print(gerador_quadrados)  # Saída: <generator object quadrados_gerador at 0x...>

# Para obter os valores:
for num in gerador_quadrados:
    print(num)