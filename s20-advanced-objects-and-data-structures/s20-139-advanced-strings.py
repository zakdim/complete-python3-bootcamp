def s20_139():
    s = 'hello world'
    print(s.capitalize())
    print(s.upper())
    print(s.lower())

    print(s.count('o'))
    print(s.find('o'))

    print(s.center(20, 'z'))

    print('hello\thi')
    print('hello\thi'.expandtabs())

    s = 'hello'
    print(s.isalnum())
    print(s.isalpha())
    print(s.islower())
    print(s.isspace())
    print(s.istitle())
    print(s.isupper())
    print('HELLO'.isupper())

    print(s.endswith('o'))
    print(s[-1])

    # String regex
    print(s.split('e'))
    print('hiihiahihihasdfihi'.split('i'))
    print('hiihiahihihasdfihi'.partition('i'))


if __name__ == '__main__':
    s20_139()