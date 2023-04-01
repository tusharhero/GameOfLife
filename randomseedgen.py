import random

density = 1

size = (100, 100)
print(size)

for _ in range(int(size[0] * size[1] * density)):
    i = random.randrange(size[0])
    j = random.randrange(size[1])
    print((i, j))
