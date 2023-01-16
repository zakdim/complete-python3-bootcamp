# python one.py

def func():
    print("FUNC() in ONE.PY")


def function():
    pass


def function2():
    pass


print("TOP LEVEL IN ONE.PY")

if __name__ == "__main__":
    # RUN THE SCRIPT!
    print('ONE.PY is being run directly!')
    function2()
    function()
else:
    print('ONE.PY has been imported!')
