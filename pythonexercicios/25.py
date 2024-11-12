values = input()

l = [int(x) for x in values.split(",")]
t = tuple(l)

print(l)
print(t)

soma = 0

for numero in l:
    soma += numero

print(f'A soma e {soma}')