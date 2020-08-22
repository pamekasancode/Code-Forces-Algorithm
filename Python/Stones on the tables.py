def solve():
	length = int(input())
	seq = [x for x in input()]
	new_seq = []
	
	prev = None
	i = 0

	for col in seq:
		if i == 0:
			prev = col
		else:
			if prev == col:
				new_seq.append(col)	
			prev = col
		i += 1

	print(len(new_seq))

solve()
