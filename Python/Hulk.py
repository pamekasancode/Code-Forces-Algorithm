def solve():
	n = int(input())
	i = 0
	seq = []

	for _ in range(n):
		if i % 2 == 0:
			seq.append("I hate ")
		else:
			seq.append("I love ")
		i += 1

	last = seq.pop() + "it"
	seq2 = []
	for _ in range(len(seq)):
		# print(seq, x)
		char = seq.pop(0) + "that"
		seq2.append(char)
	seq2.append(last)

	d = [print(x, end=" ") for x in seq2]
	print("\n")

solve()
