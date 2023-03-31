import random

size = (50, 50)
print(size)

for i in range(random.randrange(min(size))):
    for j in range(random.randrange(min(size))):
        print((i,j))
