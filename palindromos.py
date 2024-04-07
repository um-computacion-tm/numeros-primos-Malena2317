import unittest

class Testpalindrome(unittest.TestCase):
    def test_a(self):
        resultado = is_palindrome ('a')
        self.assertEqual(resultado,True)

        
unittest.main()

