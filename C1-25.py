def remove_puntuation(aa):
    """Remove punctuation from a string."""
    letters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for char in aa:
        if char not in letters:
            aa = aa.replace(char, '')
    return aa

def readable_removepuntuation(aa):
    """Remove punctuation from a string, keeping only letters and spaces."""
    result = []
    for char in aa:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or char == ' ':
            result.append(char) # keep letters and spaces
        else:
            result.append(' ') # replace punctuation with space
    return ''.join(result) # join the list into a string

a = input("Enter a string: ")
print(readable_removepuntuation(a))
