import inspect
import re
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

    return method_dict

