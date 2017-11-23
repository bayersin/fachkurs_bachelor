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
        while answer != '7':
            answer = input('Was ist der Inhalt von y?')
        print('Richtig!\n')
        
    def test_02(self):
        print('--------------------------------------------')
        print('Frage:')
        print('x = 5')
        print('y = 2')
        print('z = x == y')
        answer = None
        while answer != "False":
            answer = (input('Was ist der Inhalt von y?'))
        print('Richtig!\n')
        
    def test_03(self):
        print('--------------------------------------------')
        print('Frage:')
        print('x = 5')
        print('y = 2')
        print('z = x%y')
        answer = None
        while answer != '1':
            answer = input('Was ist der Inhalt von y?')
        print('Richtig!\n')
        
    def test_04(self):
        print('--------------------------------------------')
        print('Frage:')
        print('numbers = [1,2,3,4,5,6,7,8,9]')
        print('sum = 0')
        print('for x in numbers:')
        print('    sum = sum + x')
        answer = None
        while answer != '45':
            answer = input('Welchen Wert hat sum?')
        print('Richtig!\n')
        
    def test_05(self):
        print('--------------------------------------------')
        print('Frage:')
        print('x = 5')
        print('if x == 2:')
        print('    y = 3')
        print('else:')
        print('    y = 50')
        answer = None
        while answer != '50':
            answer = input('Welchen Wert hat y?')
        print('Richtig!\n')
        

    def test_06(self):
        print('--------------------------------------------')
        print('Frage:')
        print('x = 1')
        print('def my_func():')
        print('\t x = 2\n')
        print('print(x)')
        answer = None
        while answer != '1':
            answer = input('Was wird der print-Befehl ausgeben?')
        print('Richtig!\n')
        
    def test_07(self):
        print('--------------------------------------------')
        print('Frage:')
        print('x = 1')
        print('def my_func():')
        print('\t x = 2')
        print('\t print(x)')
        answer = None
        while answer != '2':
            answer = input('Was wird der print-Befehl ausgeben?')
        print('Richtig!\n')


    def test_08(self):
        print('--------------------------------------------')
        print('Frage:')
        print('l = [1,2,3,4]')
        answer = None
        while answer != '2':
            answer = input('Was ist die Länge von l[1:3]')
        print('Richtig!\n')

    def test_09(self):
        print('--------------------------------------------')
        print('Frage:')
        print('l = [1,2,3,4]')
        answer = None
        while answer != '3':
            answer = input('Welche Zahl ist l[2]?')
        print('Richtig!\n')

    def test_10(self):
        print('--------------------------------------------')
        print('Frage:')
        print('l = [1,2,3,4]')
        print('l2 = l')
        print('l.append("meep")')
        answer = None
        while answer != '5':
            answer = input('Wie viele Elemente enthält l2?')
        print('Richtig!\n')

    def test_11(self):
        print('--------------------------------------------')
        print('Frage:')
        print('l = [1,2,3,4,5]')
        print('l.extend([6,7,8])')
        answer = None
        while answer != '8':
            answer = input('Was ist die Länge von l?')
        print('Richtig!\n')

    def test_12(self):
        print('--------------------------------------------')
        print('Frage:')
        print('l = [1,2,3,4,5]')
        print('l.append([6,7,8])')
        answer = None
        while answer != '6':
            answer = input('Was ist die Länge von l?')
        print('Richtig!\n')    

    def test_13(self):
        print('--------------------------------------------')
        print('l = [1,2,3,4]')
        print('a = l.append(5)')
        answer = None
        while answer != 'None':
            answer = input('Was ist a?')
        print('Richtig!\n')

    def test_14(self):
        print('--------------------------------------------')
        print('def my_func(l=[]):')
        print('\tl.append("item")')
        print('\treturn l')
        print('a = my_func()')
        print('b = my_func()')
        answer = None
        answer2 = None
        while answer != '2':
            answer = input('Was ist die Länge von a?')
        while answer2 != '2':
            answer2 = input('Was ist die Länge von b?')

    def test_15(self):
        print('--------------------------------------------')
        print('numbers = [1,2,3,4,5,6,7,8,9]')
        print('sum = 0')
        print('for x in numbers:')
        print('\tif x%2 == 0:')
        print('\t\tsum = sum + x')
        answer = None
        while answer != '20':
            answer = input('Welchen Wert hat sum?')

    def test_16(self):
        print('--------------------------------------------')
        print('x = 10')
        print('i = 0')
        print('while i <= x:')
        print('\ti = i + 1')
        print('print(i)')
        answer = None
        while answer != '11':
            answer = input('Was gibt der print Befehl aus?')

    def test_17(self):
        print('--------------------------------------------')
        print('x = 10')
        print('i = 0')
        print('y = 0')
        print('while i <= x:')
        print('\ty = y + i')
        print('\ti = i + 1')
        print('print(y)')
        answer = None
        while answer != '55':
            answer = input('Was gibt der print Befehl aus?')

    def test_18(self):
        print('--------------------------------------------')
        print('x = 10')
        print('i = 0')
        print('y = 0')
        print('while i <= x:')
        print('\ti = i + 1')
        print('\ty = y + i')
        print('print(y)')
        answer = None
        while answer != '66':
            answer = input('Was gibt der print Befehl aus?')

    def test_19(self):
        print('--------------------------------------------')
        print('x = 10')
        print('i = 0')
        print('y = 0')
        print('while i < x:')
        print('\ti = i + 1')
        print('\ty = y + i')
        print('print(y)')
        answer = None
        while answer != '55':
            answer = input('Was gibt der print Befehl aus?')


    def test_20(self):
        print('--------------------------------------------')
        print('x = 10')
        print('i = 0')
        print('y = 0')
        print('i2 = 0')
        print('y2 = 0')
        print('while i <= x:')
        print('\ty = i + y')
        print('\ti = i + 1')
        print('while i2 < x:')
        print('\ti2 = i2 + 1')
        print('\ty2 = y2 + i2')
        print('z = str(y == y2)')
        answer = None
        while answer != '4':
            answer = input('Wie viele Zeichen hat z?')

    def test_21(self):
        print('--------------------------------------------')
        print('x = 10')
        print('i = 0')
        print('y = 0')
        print('i2 = 0')
        print('y2 = 0')
        print('while i <= x:')
        print('\ty = i + y')
        print('\ti = i + 1')
        print('while i2 < x:')
        print('\ti2 = i2 + 1')
        print('\ty2 = y2 + i2')
        print("z = str('y == y2')")
        answer = None
        while answer != '7':
            answer = input('Wie viele Zeichen hat z?')

    def test_22(self):
        print('--------------------------------------------')
        print('answer = None')
        print('i = 7')
        print('while answer != 7:')
        print('\ti = i + 3')
        print('\tanswer = i%8')
        print('\tprint(answer)')
        answer1 = None
        answer2 = None

        while answer1 != '8':
            answer1 = input('Wie oft wird der print Befehl ausgeführt?')
        print('\n')
        while answer2 != '31':
            answer2 = input('Welchen Wert hat i, wenn der print Befehl das letzte mal ausgeführt wird?') 

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