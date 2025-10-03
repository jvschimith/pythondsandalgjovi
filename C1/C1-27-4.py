def gerador_nomes():
    nomes = ["Alice", "Bob", "Carlos"]
    for nome in nomes: # is the same that write for i in range(len(nomes)):
        yield nome # is the same that yield i

# Criando o gerador
gen = gerador_nomes()

# Imprimindo apenas o primeiro nome
print(next(gen))  # Saída: "Alice"

# Se chamar next() de novo, pega o próximo:
print(next(gen))  # Saída: "Bob"

print(next(gen))  # Saída: "Carlos"