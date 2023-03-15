def print_value(label, value=''):
    print(f'{label}:\n{"=" * 30}\n{value}')


def int_stream():
    num = 0
    while True:
        yield num
        num += 1
