def solve():
	b1 = [int(x) for x in str(input())]
	b2 = [int(x) for x in str(input())]
	res = ["0" if b1[x] == b2[x] else "1" for x in range(len(b1))]
	print("".join(res))

solve()
