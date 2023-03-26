from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets


def func(x):
    return x


def s21_147():
    interact(func, x=10)


if __name__ == '__main__':
    s21_147()
