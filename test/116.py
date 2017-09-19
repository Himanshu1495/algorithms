import sys
sys.path.insert(0,'../solutions/')
from sol116 import flatten_array
import unittest

class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(flatten_array([1,2,[3,4,5],[6,[7,8]],9]),[1,2,3,4,5,6,7,8,9])

unittest.main()
