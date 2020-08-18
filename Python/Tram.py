def solve():
    tram = int(input())
    seq = []
    i = 0
    i2 = 0
    while i < tram:
        chrs = list(map(int, input().split()))
        if i == 0:
            i2 += sum(chrs)
            seq.append(i2)

        elif chrs[1] == 0:
            seq.append(i2)
            i2 -= chrs[0] + chrs[1]
        else:
            i2 -= chrs[0] + chrs[1]
            seq.append(i2)
        i += 1

    return max(seq)

print(solve())