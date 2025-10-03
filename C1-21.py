def reversed_output():
    try:
        while True:
            a = input().split()
            print(" ".join(a[::-1]))
    except EOFError:
        pass

reversed_output()