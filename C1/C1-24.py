def vowels_legible(aa):
    """Return the number of vowels in a string, with a more readable implementation."""
    count = 0
    vowels_set = {'a', 'e', 'i', 'o', 'u'}
    for char in aa.lower():
        if char in vowels_set:
            count += 1
    return count

def vowels_legible2(aa):
    """Return the number of vowels in a string, without using 'in'."""
    count = 0
    for char in aa.lower():
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            count += 1
    return count

a = input("Enter a string: ")
print("Number of vowels (using 'in'):", vowels_legible(a))