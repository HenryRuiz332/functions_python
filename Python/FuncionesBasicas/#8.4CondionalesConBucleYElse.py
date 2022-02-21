email = input("Introduce tu Email: ");

for i in email:
	if i == "@":
		arroba = True
		break; #Sale i continua
else:
	arroba = False;

print(arroba);