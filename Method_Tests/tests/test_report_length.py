from lib.report_length import *

def test_no_length():
    assert report_length('') == 'This string was 0 characters long.'
def test_ten_chars():
    assert report_length('TestWord10') == 'This string was 10 characters long.'
def test_10000_chars():
    word = ''
    for i in range(123456):
        word += 'a'
    assert report_length(word) == 'This string was %d characters long.' %(len(word))