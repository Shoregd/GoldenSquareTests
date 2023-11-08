from lib.password_checker import *
import pytest

def test_invalid_password():
   test_checker = PasswordChecker()
   with pytest.raises(Exception) as e:
      test_checker.check('Taco')
   err_message = str(e.value)
   assert err_message == 'Invalid password, must be 8+ characters.'
def test_valid_password():
   test_checker = PasswordChecker()
   assert test_checker.check('Tacosareawesome') == True
def test_exactly_valid():
   test_checker = PasswordChecker()
   assert test_checker.check('TacoTaco') == True
def test_error_when_one_char_short():
   test_checker = PasswordChecker()
   with pytest.raises(Exception) as e:
      test_checker.check('TacoTac')
   err_message = str(e.value)
   assert err_message == 'Invalid password, must be 8+ characters.'