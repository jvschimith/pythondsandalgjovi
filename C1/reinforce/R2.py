# Function is even without using multiplication, mod or division operators

def is_even(num):
    
    """ Here we are using the bitwise operation, with the operator AND, always with the number 1, cause the last even number will have their last bit in 0, while an odd number will have their last bit in 1;

    Remember that: Any number AND 0, is zero, therefore, to be One, the two needs to be One
    """
    if  (num & 1) == 0:
         return f"The num {num} is even"
    else:
         return f"The num {num} is odd"

# Testing
num1 = 10
num2 = 7

print(is_even(num1))
print(is_even(num2))


