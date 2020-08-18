def solve():
    wrds = list(set(str(input()).lower()))

    if len(wrds) % 2 == 0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"




print(solve())
