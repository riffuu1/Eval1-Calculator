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

    def test_execute_sub_get_result(self):
        # given
        math_request = MathRequest(3, 'sub', 4)

        # when
        Mathlib.execute(math_request)

        # then
        self.assertEqual(math_request.get_res(), -1)

    def test_execute_mul_get_result(self):
        # given
        math_request = MathRequest(3, 'mul', 4)

        # when
        Mathlib.execute(math_request)

        # then
        self.assertEqual(math_request.get_res(), 12)

    def test_execute_div_get_result(self):
        # given
        math_request = MathRequest(3, 'div', 4)

        # when
        Mathlib.execute(math_request)

        # then
        self.assertEqual(math_request.get_res(), 0.75)

if __name__ == '__main__':
    unittest.main()