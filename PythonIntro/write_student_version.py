import inspect
import re
import pickle as pkl
PythonTestModule = __import__('20171103_PythonTest')

def python_test_to_answer_dict(p_test):
    method_dict = {}
    list_of_tests = [method for method in dir(p_test) if not method.startswith('_')]
    
    for test in list_of_tests:
        test_lines = inspect.getsourcelines(eval('p_test.{}'.format(test)))[0]
        lines_with_answers = [l for l in test_lines if '!=' in l and not l.strip().startswith('print')]
        method_dict[test] = {}
        for line in lines_with_answers:
            match = re.search('answer[1-9]? != [\'\"](.+?)[\'\"]', line)
            if match:
                result = match.group()
                method_dict[test][result.split('!=')[0].strip()] = result.split('!=')[1].strip()[1:-1]
    
    pkl_file = open('answer_dict.pkl', 'wb')
    pkl.dump(method_dict, pkl_file)
    pkl_file.close()
    return method_dict

def write_student_version(p_test, answer_dict):
    all_methods = []
    for method in answer_dict:
        current_method = eval('inspect.getsourcelines(p_test.{})[0]'.format(method))
        for answer in answer_dict[method]:
            for i, line in enumerate(current_method):
                if '!=' in line and not line.strip().startswith('print'):
                    m = re.search('{} != [\'\"]{}[\'\"]'.format(answer, answer_dict[method][answer]), line)
                    if m:
                        #print(m)
                        #print(line)
                        r = re.sub('[\'\"]{}[\'\"]'.format(answer_dict[method][answer]), 'answer_dict[\'{}\'][\'{}\']'.format(method,answer), line)
                        #print(r)
                        current_method[i] = r
        all_methods.append(current_method)
    

    all_methods_flat = [''.join(l) for l in all_methods]
    all_methods_str = '\n'.join(all_methods_flat)

    new_module = open("StudentPythonTest.py", "w")
    new_module.write('import numpy as np\n')
    new_module.write('import pickle as pkl\n')
    new_module.write('import inspect\n\n\n')
    new_module.write('class PythonTest:\n')
    new_module.write('    def __init__(self):\n')
    new_module.write('        pass\n\n')
    new_module.write(all_methods_str)
    new_module.write('\n\n')
    new_module.write('if __name__ == "__main__":\n')
    new_module.write('    pkl_file = open("answer_dict.pkl", "rb")\n')
    new_module.write('    answer_dict = pkl.load(pkl_file)\n')
    new_module.write('    pkl_file.close()\n')
    new_module.write('    test = PythonTest()\n')
    new_module.write('    attrs = (getattr(test, name) for name in dir(test))\n')
    new_module.write('    methods = filter(inspect.ismethod, attrs)\n')
    new_module.write('    for method in methods:\n')
    new_module.write('        try:\n')
    new_module.write('            method()\n')
    new_module.write('        except TypeError:\n')
    new_module.write('            pass')
    return all_methods


if __name__ == '__main__':
    p_t = PythonTestModule.PythonTest()
    answer_dict = python_test_to_answer_dict(p_t)
    all_methods = write_student_version(p_t, answer_dict)
