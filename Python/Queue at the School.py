def solve():
	nums = list(map(int, input().split()))
	seq = [x for x in str(input())]
	length = nums[0]
	time = nums[1]			# BGGBG input, time = 1
	
	prev = None
	i = 0
	for _ in range(time):
		for x in seq:
			if i == 0:
				prev = x
			else:
				if prev == "B" and x == "G":
					seq.insert(i, seq.pop(i-1))
				prev = x
			i += 1
		i = 0

	print("".join(seq))

solve()
