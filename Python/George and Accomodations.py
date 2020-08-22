def solve():
	rooms = int(input())
	i = 0
	for _ in range(rooms):
		d = list(map(int, input().split()))
		acc = d[1]
		people = d[0]

		if acc - people >= 2:
			i += 1

	print(i)

solve()
