def solve():
	year_d = int(input())

	while True:
		year_d += 1
		sort = set(str(year_d))

		if len(sort) >= 4:
			break

	print(year_d)

solve()
