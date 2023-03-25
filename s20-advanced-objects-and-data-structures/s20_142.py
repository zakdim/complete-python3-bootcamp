def s20_142():
    l = [1, 2, 3]
    print(l)
    l.append(4)
    print(l)

    print(l.count(10))
    print(l.count(1))

    x = [1, 2, 3]
    x.append([4, 5])
    print(x)

    x = [1, 2, 3]
    x.extend([4, 5])
    print(x)

    print(l.index(2))
    try:
        print(l.index(10))
    except ValueError as ex:
        print(f'Caught exception: {ex}')

    l.insert(2, 'inserted')
    print(l)

    elem = l.pop()
    print(elem, l)
    elem = l.pop(0)
    print(elem, l)

    elem = l.remove('inserted')
    print(elem, l)
    l = [1, 2, 3, 4, 3]
    l.remove(3)
    print(l)

    l.reverse()
    print(l)

    l.sort()
    print(l)


if __name__ == '__main__':
    s20_142()
