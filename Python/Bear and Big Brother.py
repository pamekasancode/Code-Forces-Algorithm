def solve():
	p = list(map(int, input().split()))
	w1 = p[0]
	w2 = p[1]
	i = 0
	while w1 <= w2:
		w1 *= 3
		w2 *= 2
		i += 1

	print(i)

solve()
