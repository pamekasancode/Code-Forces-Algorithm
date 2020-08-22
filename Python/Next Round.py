def solve():
	nums = list(map(int, input().split()))
	ranges = nums[0]
	req = nums[1]
	seq = list(map(int, input().split()))
	
	d = 0
	for x in seq:
		if x >= seq[req-1] and x > 0:
			d += 1

	print(d)

solve()
