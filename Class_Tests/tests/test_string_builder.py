from lib.string_builder import *

def test_init_of_class():
    word = StringBuilder()
    assert word.size() == 0
    assert word.output() == ''
def test_add_single_string():
    word = StringBuilder()
    test_str = 'test'
    word.add(test_str)
    assert word.size() == len(test_str)
    assert word.output() == test_str
def test_add_multiple_strings():
    word = StringBuilder()
    str_list = ['Taco','Acto','Cato','Octa']
    for i in range(len(str_list)):
        word.add(str_list[i])
        assert word.size() == (i+1) * len(str_list)
    assert word.output() == 'TacoActoCatoOcta'