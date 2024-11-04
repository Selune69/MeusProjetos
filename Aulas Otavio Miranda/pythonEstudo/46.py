def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n > 10:
            return


gen = generator(n=5, maximum=8)

for n in gen:
    print(n)