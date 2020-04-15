str = input()

for dif in range(26):
	out = ""
	cnt = 0
	print(dif, end=": ")
	for c in list(str):
		if c.islower():
			out += chr((ord(c) - ord('a') + dif) % 26 + ord('a'))
		elif c.isupper():	
			out += chr((ord(c) - ord('A') + dif) % 26 + ord('A'))
		else:
			out += c
		cnt += 1 	
	print(out)

