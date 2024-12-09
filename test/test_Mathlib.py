import unittest

from src.Mathlib import Mathlib
from src.MathRequest import MathRequest

class TestMathlib(unittest.TestCase):

    def setUp(self):
        pass

    def test_execute_add_get_result(self):
        #given
        math_request=MathRequest(3, 'add', 4)

        #when
        Mathlib.execute(math_request)

        #then
        self.assertEqual(math_request.get_res(),7)

if __name__ == '__main__':
    unittest.main()