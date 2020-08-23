def solve():
	nums = int(input())
	present = list(map(int, input().split()))
	seq = []
	i = 1
	for x in present:
		i2 = 1
		for y in present:
			if y == i:
				seq.append(i2)
				break
			i2 += 1
		i += 1
		
	d = [print(x, end=" ") for x in seq]
