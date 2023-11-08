from lib.gratitudes import *

def test_init_of_class():
    test_class = Gratitudes()
    assert test_class.gratitudes == []
    assert test_class.format() == 'Be grateful for: '
def test_add_gratitude():
    test_class = Gratitudes()
    test_class.add('Tacos')
    assert test_class.gratitudes == ['Tacos']
    assert test_class.format() == 'Be grateful for: Tacos'
def test_add_gratitudes():
    test_class = Gratitudes()
    test_class.add('Tacos')
    test_class.add('Tasty Tacos')
    assert test_class.gratitudes == ['Tacos','Tasty Tacos']
    assert test_class.format() == "Be grateful for: Tacos, Tasty Tacos"