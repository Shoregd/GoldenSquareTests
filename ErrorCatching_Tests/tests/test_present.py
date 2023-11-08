from lib.present import *
import pytest

def test_init_of_class():
    test_class = Present()
    assert test_class.contents == None
def test_unwrap_error():
    test_class = Present()
    with pytest.raises(Exception) as e:
        test_class.unwrap()
    err_message = str(e.value)
    assert err_message == 'No contents have been wrapped.'
def test_wrap_error():
    test_class = Present()
    test_class.wrap('Tacos')
    with pytest.raises(Exception) as e:
        test_class.wrap('Taco')
    err_message = str(e.value)
    assert err_message == 'A contents has already been wrapped.'
def test_wrap():
    test_class = Present()
    test_class.wrap('Taco')
    assert test_class.contents == 'Taco'
def test_unwrap():
    test_class = Present()
    test_class.wrap('Taco')
    assert test_class.unwrap() == 'Taco'
    