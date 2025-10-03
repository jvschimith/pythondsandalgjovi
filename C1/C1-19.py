def print_alphabet():
    # Cria uma lista de letras do alfabeto, cada uma entre aspas simples
    letters = []
    for i in range(26):
        letter = chr(97 + i)  # 97 é o código ASCII para 'a'
        letters.append(f"'{letter}'")
    # Junta as letras separadas por vírgula e espaço, e coloca entre colchetes
    formatted = "[" + ", ".join(letters) + "]"
    print(formatted)

print_alphabet()