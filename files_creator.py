import random

for el in range(100):
    extents = random.choice(['jpg', 'txt', 'xlsx', 'pdf', 'vtc'])
    name = str(random.random())[2:]

    file = f'{name}.{extents}'

    with open('garbage/' + file, 'w') as fh:
        fh.write('')