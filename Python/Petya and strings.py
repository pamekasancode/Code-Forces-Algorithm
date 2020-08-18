def solve():
    str1 = str(input().lower())
    str2 = str(input().lower())

    if str1 < str2:
        print("-1")
    elif str1 > str2:
        print("1")
    else:
        print("0")

solve()
