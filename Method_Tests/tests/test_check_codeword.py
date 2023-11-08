from lib.check_codeword import *

def test_check_codeword_is_close():
    assert check_codeword('honse') == 'Close, but nope.'
def test_check_codeword_is_wrong():
    assert check_codeword('hones') == 'WRONG!'
def test_check_codeword_is_right():
    assert check_codeword('horse') == 'Correct! Come in.'
def test_close_codeword():
    assert check_codeword('honse') == 'Correct! Come in.'
def test_wrong_codeword():
    assert check_codeword('hones') == 'Correct! Come in.'