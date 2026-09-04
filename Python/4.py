def max_satisfied_teammates(expectations, cards):
    itteration = min(len(expectations),len(cards))
    dishes_sort = sorted(expectations)
    cards_sort = sorted(cards)
    n = 0
    for dish in dishes_sort:
        for j,card in enumerate(cards_sort):
            if card >= dish:
                n += 1
                del cards_sort[j]
                break
    return n
    pass
expectations = [5, 20, 1000]
cards = [10, 15, 100]
print(max_satisfied_teammates(expectations,cards))