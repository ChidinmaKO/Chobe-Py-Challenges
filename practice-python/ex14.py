def names(l):
    # list way
    new = []
    for i in l:
        if not i in new:
            new.append(i)
    # set way
    new = list(set(l))
    print(new)

names(["Michele", "Robin", "Sara", "Michele"])