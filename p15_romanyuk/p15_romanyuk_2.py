cards = ['A', *range(2,11), 'J', 'Q', 'K']
suit = ['diamods', 'clubs', 'hearts', 'spades']
g = (str(j) + ' ' + str(i) for i in suit for j in cards)
for i in range(53):
    print(next(g))