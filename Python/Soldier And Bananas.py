def solve():
    chars = str(input()).split()

    k, n, w = int(chars[0]), int(chars[1]), int(chars[2])
    tot = 0
    for x in range(1, w+1):
         tot += k*x

    n -= tot

    if "-" in str(n):
        return int("".join(str(n).split("-")))

    return 0



print(solve())
