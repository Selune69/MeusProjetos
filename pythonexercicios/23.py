l = []

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        l.append(str(i))

print(f','.join(l))

#or

print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=",")