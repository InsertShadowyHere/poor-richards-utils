import random
def random_words(ct):
    wrds = []
    with open('20k.txt', 'r') as words:
        x = words.read().split()
        for _ in range(ct):
            wrds.append(random.choice(x))
    return wrds
x = random_words(5)
print(x)