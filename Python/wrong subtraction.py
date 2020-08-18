def solve():
	inputs = list(map(int, input().split()))
	nums = inputs[0]
	times = inputs[1]

	for _ in range(times):
		if nums % 10 == 0:
			nums /= 10
		else:
			nums -= 1

	print(int(nums))

solve()



