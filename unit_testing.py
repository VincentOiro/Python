import unittest

# Define a class that inherits from unittest.TestCase
class TestStringMethods(unittest.TestCase):
   # The setUp method is called before each test method
   def setUp(self):
       pass

   # The test_strings_a method tests if a string with 4 'a's is equal to 'aaaa'
   def test_strings_a(self):
       self.assertEqual('a'*4, 'aaaa')

   # The test_upper method tests if a string converted to uppercase is equal to the expected result
   def test_upper(self):
       self.assertEqual('foo'.upper(), 'FOO')

   # The test_isupper method tests if a string is uppercase or not
   def test_isupper(self):
       # The assertTrue method checks if the first argument is True
       self.assertTrue('FOO'.isupper())
       # The assertFalse method checks if the first argument is False
       self.assertFalse('Foo'.isupper())

   # The test_strip method tests if the stripped string matches the expected result
   def test_strip(self):
       s = 'geeksforgeeks'
       self.assertEqual(s.strip('geek'), 'sforgeeks')

   # The test_split method tests if the split string matches the expected result
   def test_split(self):
       s = 'hello world'
       self.assertEqual(s.split(), ['hello', 'world'])
       # The assertRaises method checks if the first argument is raised by the second argument
       with self.assertRaises(TypeError):
           s.split(2)

# Run the tests
if __name__ == '__main__':
   unittest.main()