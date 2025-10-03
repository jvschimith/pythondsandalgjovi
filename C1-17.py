def scale(data, factor):
    for value in data:
        value *= factor
        print("\tScaled value:", value)
    

data = [1, 2, 3, 4, 5]
scaled_data = scale(data, 2)