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
        

    def test_05(self):
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
        
    def test_06jo(self):
        print('--------------------------------------------')
        print('Frage:')
        print('x = 1')
        print('def my_func():')
        print('\t x = 2')
        print('\t print(x)')
        answer = None
        while answer != 2:
            answer = int(input('Was wird der print-Befehl ausgeben?'))
        print('Richtig!\n')


    def test_07(self):
        print('--------------------------------------------')
        print('Frage:')
        print('l = [1,2,3,4]')
        answer = None
        while answer != 2:
            answer = int(input('Was ist die Länge von l[1:3]'))
        print('Richtig!\n')

    def test_08(self):
        print('--------------------------------------------')
        print('Frage:')
        print('l = [1,2,3,4]')
        answer = None
        while answer != 3:
            answer = int(input('Welche Zahl ist l[2]?'))
        print('Richtig!\n')

    def test_09(self):
        print('--------------------------------------------')
        print('Frage:')
        print('l = [1,2,3,4]')
        print('l2 = l')
        print('l.append("meep")')
        answer = None
        while answer != 5:
            answer = int(input('Wie viele Elemente enthält l2?'))
        print('Richtig!\n')

    def test_10jo(self):
        print('--------------------------------------------')
        print('Frage:')
        print('l = [1,2,3,4,5]')
        print('l.extend([6,7,8])')
        answer = None
        while answer != 8:
            answer = int(input('Was ist die Länge von l?'))
        print('Richtig!\n')

    def test_11jo(self):
        print('--------------------------------------------')
        print('Frage:')
        print('l = [1,2,3,4,5]')
        print('l.append([6,7,8])')
        answer = None
        while answer != 6:
            answer = int(input('Was ist die Länge von l?'))
        print('Richtig!\n')    

    def test12(self):
        print('--------------------------------------------')
        print('l = [1,2,3,4]')
        print('a = l.append(5)')
        answer = None
        while answer != 'None':
            answer = input('Was ist a?')
        print('Richtig!\n')

    def test13jo(self):
        print('--------------------------------------------')
        print('def my_func(l=[]):')
        print('\tl.append("item")')
        print('\treturn l')
        print('a = my_func()')
        print('b = my_func()')
        answer = None
        answer2 = None
        while answer != 2:
            answer = int(input('Was ist die Länge von a?'))
        while answer2 != 2:
            answer2 = int(input('Was ist die Länge von b?'))
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