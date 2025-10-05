# Write a short python function minmax that thakes a sequence of one or more numbers, and returns the result in the form of a tuple of lenght two. Dont use built in functions minmax.

def minmax(data):

    i = 0
    max = 0
    min = 1
    
    for i in range(len(data)):
        if (data[i] > max):
            max = data[i]
        
        if (data[i] < min):
            min = data[i]
       
    return f"({min}, {max})"

# Testing

print(minmax([1, 2, 3]))


