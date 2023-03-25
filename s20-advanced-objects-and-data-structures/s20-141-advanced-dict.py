def s20_141():
    d = {'k1': 1, 'k2': 2}

    d2 = {x: x ** 2 for x in range(10)}
    print(d2)

    d3 = {k: v ** 2 for k, v in zip(['a', 'b'], range(2))}
    print(d3)

    for k in d.items():
        print(k)
    for k, v in d.items():
        print(k, v)
    for v in d.values():
        print(v)
    for k in d.keys():
        print(k)


if __name__ == '__main__':
    s20_141()
