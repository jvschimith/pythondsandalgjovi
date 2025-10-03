list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def reverse_list(lst):
    if len(lst) == 0:
        return []
    else:
        for i in range(len(lst) // 2):
            lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i] #swap
    return lst
reverse_list(list)

print(list)