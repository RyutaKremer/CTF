import base64

input = "rKrUl+/clKHb4u/sm6sgnaPfnO/XkO=ewqPU45bRjp4gwa7NntoM467Onu/enqPRlakgj6Egjp0e1gAA"
table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
output = ""

for c in input:
	print(c, table.find(c))
	output += table[len(table) - table.find(c) - 1]

output = base64.b64decode(output.encode())
print(output)
