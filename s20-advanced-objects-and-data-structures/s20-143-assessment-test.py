def s20_143():
    # Advanced numbers
    print(bin(1024))
    print(hex(1024))

    print(round(5.23222, 2))

    # Advanced strings
    s = 'hello how are you Mary, are you feeling okay?'
    print(s.islower())
    print('?'.islower())
    s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
    print(s.count('w'))

    set1 = {2, 3, 1, 5, 6, 8}
    set2 = {3, 1, 7, 5, 6, 8}
    print(set1.difference(set2))
    print(set1.union(set2))

    d = {k: k ** 3 for k in range(5)}
    print(d)

    list1 = [1, 2, 3, 4]
    list1.reverse();
    print(list1)
    list2 = [3, 4, 2, 5, 1]
    list2.sort()
    print(list2)


if __name__ == '__main__':
    s20_143()
