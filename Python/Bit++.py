def solve():
    lines = int(input())
    i, x = 0, 0

    while (i != lines):
        state = str(input())
        if "++" in state:
            x += 1
        elif "--" in state:
            x -= 1
        else:
            print("Invalid syntax") 
        i += 1

    print(x)

solve()
