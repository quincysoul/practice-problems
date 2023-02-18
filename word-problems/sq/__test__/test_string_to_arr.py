import unittest
from sq.string_to_arr import Solution

class Test(unittest.TestCase):
    def test_expected_sock(self):
        "Should return matched socks if there are some."
        solution = Solution()
        answer = [
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
        ]
        input = ('0010001001100100', 4, 4)
        res = solution.string_to_arr(*input)
        self.assertEqual(answer, res)
    # def test_expected_nosock(self):
    #     "Should return no matched socks if there are none."
    #     solution = Solution()
    #     answer = []
    #     input = [(1, 'left', 'red'), (2, 'left', 'orange'), (3, 'left', 'orange')]
    #     self.assertEqual(answer, solution.sock_match(input))
