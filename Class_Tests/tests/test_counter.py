from lib.counter import *

def test_base_counter():
    result = Counter()
    assert result.report() == 'Counted to 0 so far.'

def test_add_to_counter():
    result = Counter()
    result.add(6)
    assert result.count == 6
    assert result.report() == 'Counted to 6 so far.'
def test_add_negative():
    result = Counter()
    result.add(-12)
    assert result.count == -12
    assert result.report() == 'Counted to -12 so far.'