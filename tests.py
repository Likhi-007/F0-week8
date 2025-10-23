import unittest
from main import to_upper
class MyTestCase(unittest.TestCase): def test_to_upper(self):
name = "Tejaswi" 
upper_name = to_upper(name)
self.assertEqual(upper_name, "Tejaswi")

if 	name	== '	main	': unittest.main() 

