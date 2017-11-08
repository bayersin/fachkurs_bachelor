import numpy as np
import inspect
# from itertools import ifilter

class PythonTest:
    def __init__(self):
        pass

    def test_01(self):
        print('--------------------------------------------')
        print('Frage:')
        print('x = 7')
        print('y = x')
        print('x = 3')
        answer = None
        while answer != 7:
            answer = int(input('Was ist der Inhalt von y?'))
        print('Richtig!\n')

    def test_02(self):
        print('--------------------------------------------')
        print('Frage:')
        print('x = 1')
        print('def my_func():')
        print('\t x = 2\n')
        print('print(x)')
        answer = None
        while answer != 1:
            answer = int(input('Was wird der print-Befehl ausgeben?'))
        print('Richtig!\n')

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