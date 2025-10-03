from random import randint 
datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def randomize_list(data):
    for i in range(len(data)):
        j = randint(0, len(data) - 1)  # Generate a random index
        data[i], data[j] = data[j], data[i]  # Swap elements at indices i and j
    return data

print(randomize_list(datas))