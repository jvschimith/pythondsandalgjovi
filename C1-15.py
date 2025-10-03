a = input().split()

def are_different(a):
    for i in range(len(a)):
        if a[i] == a[(i + 1) % len(a)]: # check if current element is the same as the next
            return False # if they are the same, return False
        else:
            continue # if they are different, continue checking
    return True

if are_different(a) == 1:
    print("YES")
else:  
    print("NO")

