my = []
find = int(input("Enter a number to look for"))

found = False

for i in range(find):
	val = float(input("Enter a list: "))
	my.append(val)
print (val)
for d in range (len(my)):
	found = my[d] == find
	if found:
		break

if found:
	print("found here: ", d)
else:
	print("absent")
