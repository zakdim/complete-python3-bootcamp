def s20_140():
    s = set()
    s.add(1)
    s.add(2)
    s.add(2)
    print(s)

    s.clear()
    print(s)

    s = {1, 2, 3}
    sc = s.copy()
    print(sc)
    s.add(4)
    print(s)
    print(sc)

    diff = s.difference(sc)
    print(diff)

    s1 = {1, 2, 3}
    s2 = {1, 4, 5}
    s1.difference_update(s2)
    print(s1)

    print(s)
    s.discard(2)
    s.discard(12)
    print(s)

    s1 = {1, 2, 3}
    s2 = {1, 2, 4}
    inter = s1.intersection(s2)
    print(inter)
    s1.intersection_update(s2)
    print(s1)

    s1 = {1, 2}
    s2 = {1, 2, 4}
    s3 = {5}
    print(s1.isdisjoint(s2))
    print(s1.isdisjoint(s3))
    print(s1.issubset(s2))
    print(s2.issuperset(s1))

    print(s1.symmetric_difference(s2))

    print(s1.union(s2))
    s1.update(s2)
    print(s1)


if __name__ == '__main__':
    s20_140()
