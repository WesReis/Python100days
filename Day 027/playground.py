def add(*args):
    result = 0
    for n in args:
        result += int(n)
    return result

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)