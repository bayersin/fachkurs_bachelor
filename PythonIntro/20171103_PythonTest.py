import numpy as np
import inspect
import pickle
# from itertools import ifilter

class PythonTest:
    def __init__(self, solpath):
        pickle_in = open(solpath,"rb")
        self.sol = pickle.load(pickle_in)

    def test_01(self):
        print('--------------------------------------------')
        print('Frage 1:')
        print('x = 7')
        print('y = x')
        print('x = 3')
        answer = None
        while answer != self.sol['01']:
            answer = input('Was ist der Inhalt von y?')
        print('Richtig!\n')
        
    def test_02(self):
        print('--------------------------------------------')
        print('Frage 2:')
        print('x = 5')
        print('y = 2')
        print('z = x == y')
        answer = None
        while answer != self.sol['02']:
            answer = (input('Was ist der Inhalt von z?'))
        print('Richtig!\n')
        
    def test_03(self):
        print('--------------------------------------------')
        print('Frage 3:')
        print('x = 5')
        print('y = 2')
        print('z = x%y')
        answer = None
        while answer != self.sol['03']:
            answer = input('Was ist der Inhalt von z?')
        print('Richtig!\n')
        
    def test_04(self):
        print('--------------------------------------------')
        print('Frage 4:')
        print('numbers = [1,2,3,4,5,6,7,8,9]')
        print('sum = 0')
        print('for x in numbers:')
        print('    sum = sum + x')
        answer = None
        while answer != self.sol['04']:
            answer = input('Welchen Wert hat sum?')
        print('Richtig!\n')
        
    def test_05(self):
        print('--------------------------------------------')
        print('Frage 5:')
        print('x = 5')
        print('if x == 2:')
        print('    y = 3')
        print('else:')
        print('    y = 50')
        answer = None
        while answer != self.sol['05']:
            answer = input('Welchen Wert hat y?')
        print('Richtig!\n')
        

    def test_06(self):
        print('--------------------------------------------')
        print('Frage 6:')
        print('x = 1')
        print('def my_func():')
        print('\t x = 2\n')
        print('print(x)')
        answer = None
        while answer != self.sol['06']:
            answer = input('Was wird der print-Befehl ausgeben?')
        print('Richtig!\n')
        
    def test_07(self):
        print('--------------------------------------------')
        print('Frage 7:')
        print('x = 1')
        print('def my_func():')
        print('\t x = 2')
        print('\t print(x)')
        answer = None
        while answer != self.sol['07']:
            answer = input('Was wird der print-Befehl ausgeben?')
        print('Richtig!\n')

    def test_08(self):
        print('--------------------------------------------')
        print('Frage 8:')
        print('l = [1,2,3,4]')
        answer = None
        while answer != self.sol['08']:
            answer = input('Was ist die Länge von l[1:3]')
        print('Richtig!\n')

    def test_09(self):
        print('--------------------------------------------')
        print('Frage 9:')
        print('l = [1,2,3,4]')
        answer = None
        while answer != self.sol['09']:
            answer = input('Welche Zahl ist l[2]?')
        print('Richtig!\n')

    def test_10(self):
        print('--------------------------------------------')
        print('Frage 9:')
        print('l = [1,2,3,4]')
        answer = None
        while answer != self.sol['10']:
            answer = input('Welche Zahl ist l[-1]?')
        print('Richtig!\n')

    def test_10(self):
        print('--------------------------------------------')
        print('Frage 10:')
        print('l = [1,2,3,4]')
        print('l2 = l')
        print('l.append("meep")')
        answer = None
        while answer != self.sol['10']:
            answer = input('Wie viele Elemente enthält l2?')
        print('Richtig!\n')

    def test_11(self):
        print('--------------------------------------------')
        print('Frage 11:')
        print('l = [1,2,3,4,5]')
        print('l.extend([6,7,8])')
        answer = None
        while answer != self.sol['11']:
            answer = input('Was ist die Länge von l?')
        print('Richtig!\n')

    def test_12(self):
        print('--------------------------------------------')
        print('Frage 12:')
        print('l = [1,2,3,4,5]')
        print('l.append([6,7,8])')
        answer = None
        while answer != self.sol['12']:
            answer = input('Was ist die Länge von l?')
        print('Richtig!\n')    

    def test_13(self):
        print('--------------------------------------------')
        print('Frage 13:')
        print('l = [1,2,3,4]')
        print('a = l.append(5)')
        answer = None
        while answer != self.sol['13']:
            answer = input('Was ist a?')
        print('Richtig!\n')

    def test_14(self):
        print('--------------------------------------------')
        print('Frage 14:')
        print('def my_func(l=2):')
        print('\treturn l')
        print('a = my_func()')
        print('b = my_func(7)')
        answer = None
        answer2 = None
        while answer != self.sol['14a']:
            answer = input('Was ist a?')
        while answer2 != self.sol['14b']:
            answer2 = input('Was ist b?')

    def test_15(self):
        print('--------------------------------------------')
        print('Frage 15:')
        print('numbers = [1,2,3,4,5,6,7,8,9]')
        print('sum = 0')
        print('for x in numbers:')
        print('\tif x%2 == 0:')
        print('\t\tsum = sum + x')
        answer = None
        while answer != self.sol['15']:
            answer = input('Welchen Wert hat sum?')

    def test_16(self):
        print('--------------------------------------------')
        print('Frage 16:')
        print('x = 3')
        print('i = 0')
        print('while i <= x:')
        print('\ti = i + 1')
        print('print(i)')
        answer = None
        while answer != self.sol['16']:
            answer = input('Was gibt der print Befehl aus?')

    def test_17(self):
        print('--------------------------------------------')
        print('Frage 17:')
        print('x = 3')
        print('i = 0')
        print('y = 0')
        print('while i <= x:')
        print('\ty = y + i')
        print('\ti = i + 1')
        print('print(y)')
        answer = None
        while answer != self.sol['17']:
            answer = input('Was gibt der print Befehl aus?')

    def test_18(self):
        print('--------------------------------------------')
        print('Frage 18:')
        print('x = 3')
        print('i = 0')
        print('y = 0')
        print('while i <= x:')
        print('\ti = i + 1')
        print('\ty = y + i')
        print('print(y)')
        answer = None
        while answer != self.sol['18']:
            answer = input('Was gibt der print Befehl aus?')

    def test_19(self):
        print('--------------------------------------------')
        print('Frage 19:')
        print('x = 3')
        print('i = 0')
        print('y = 0')
        print('while i < x:')
        print('\ti = i + 1')
        print('\ty = y + i')
        print('print(y)')
        answer = None
        while answer != self.sol['19']:
            answer = input('Was gibt der print Befehl aus?')

    def test_20(self):
        print('--------------------------------------------')
        print('Frage 20:')
        print('def return_second(my_list):')
        print('\tsecond_item = my_list[x]')
        print('\treturn second_item\n')
        print('a_list = [2,7,6,1]')
        print('print(return_second(a_list))\n')
        print('7')
        answer = None
        while answer != self.sol['20']:
            answer = input('Was muss x sein, der oben stehende Code stimmt?')

    def test_21(self):
        print('--------------------------------------------')
        print('Frage 21:')
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
        while answer != self.sol['21']:
            answer = input('Wie viele Zeichen hat z?')

    def test_22(self):
        print('--------------------------------------------')
        print('Frage 22:')
        print('answer = None')
        print('i = 7')
        print('while answer != 7:')
        print('\ti = i + 3')
        print('\tanswer = i%8')
        print('\tprint(answer)')
        answer1 = None
        answer2 = None

        while answer1 != self.sol['22a']:
            answer1 = input('Wie oft wird der print Befehl ausgeführt?')
        print('\n')
        while answer2 != self.sol['22b']:
            answer2 = input('Welchen Wert hat i, wenn der print Befehl das letzte mal ausgeführt wird?') 

    def test_23(self):
        print('--------------------------------------------')
        print('Frage 23:')
        print('def my_func(my_list):')
        print('\tmy_list.append(42)\n')
        print('other_list = []')
        print('my_func(other_list)')
        print('print(other_list)')
        answer = None
        while answer != self.sol['23']:
            answer = input('Was gibt der print-Befehl aus?')

    def test_24(self):
        print('--------------------------------------------')
        print('Frage 24:')
        print('def my_func(my_int):')
        print('\tmy_int = my_int + 1\n')
        print('other_int = 3')
        print('my_func(other_int)')
        print('print(other_int)')
        answer = None
        while answer != self.sol['24']:
            answer = input('Was gibt der print-Befehl aus?')

    def test_25(self):
        print('--------------------------------------------')
        print('Frage 25:')
        print('def my_func(my_int):')
        print('\tmy_int = my_int + 1\n')
        print('\treturn my_int\n')
        print('other_int = 3')
        print('other_int = my_func(other_int)')
        print('print(other_int)')
        answer = None
        while answer != self.sol['25']:
            answer = input('Was gibt der print-Befehl aus?')



if __name__ == "__main__":
    test = PythonTest('sol.pkl')
    attrs = (getattr(test, name) for name in dir(test))
    methods = filter(inspect.ismethod, attrs)
    methods = sorted(methods, key=lambda x: str(x))
    for method in methods:
        try:
            method()
        except TypeError:
            # Can't handle methods with required arguments.
            pass