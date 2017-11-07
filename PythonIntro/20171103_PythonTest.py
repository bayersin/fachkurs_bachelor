import numpy as np
import inspect
# from itertools import ifilter

class PythonTest:
    def __init__(self):
        pass

    def test1(self):
        print('x = 7')
        print('y = x')
        print('x = 3')
        answer = None
        while answer != 7:
            answer = int(input('Was ist der Inhalt von y?'))
        print('Richtig!')

if __name__ == "__main__":
    test = PythonTest()
    attrs = (getattr(test, name) for name in dir(test))
    methods = filter(inspect.ismethod, attrs)
    for method in methods:
        try:
            method()
        except TypeError:
            # Can't handle methods with required arguments.
            pass