size = 10
a = [0] * size

def attack(bb):
    try:
        for i in range(len(bb)):
            a[i] = (int(bb[i]))
        print(a)      
    except IndexError:
        print("Don’t try buffer overflow attacks in Python!")
    
        
b = input().split()

attack(b)
print("End of the program.")