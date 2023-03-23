"""
Name: fizzbuzz.py
A program that prints the numbers from 1 to 100. But for multiples of three print “Fizz”
and for the multiples of five print “Buzz”. For numbers which are multiples of both three
and five print “FizzBuzz”. The output format is arbitrary.
"""


def print_num(n, label=''):
    print(f'{n:03d}{f" {label}" if label != "" else ""}')


def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print_num(n, 'FizzBuzz')
        elif n % 3 == 0:
            print_num(n, 'Fizz')
        elif n % 5 == 0:
            print_num(n, 'Buzz')
        else:
            print_num(n)


if __name__ == '__main__':
    fizzbuzz()
