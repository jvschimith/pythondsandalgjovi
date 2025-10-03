def arithmetic_possible(a, b, c):
    if a + b == c:
        return print("Yes, it is possible to get the result by adding the first two numbers.")
    elif a - b == c:
        return print("Yes, it is possible to get the result by subtracting the second number from the first.")
    elif a * b == c:
        return print("Yes, it is possible to get the result by multiplying the first two numbers.")
    elif a / b == c:
        return print("Yes, it is possible to get the result by dividing the first number by the second.")
    else:
        return print("No, it is not possible to get the result with the given operations.")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the result number: "))

arithmetic_possible(a, b, c)