import unittest
from sq.sock_match import Solution

class Test(unittest.TestCase):
    def test_expected_sock(self):
        "Should return matched socks if there are some."
        solution = Solution()
        answer = [(2,1, 'red')]
        input = [(1, 'left', 'red'), (2, 'right', 'red'), (3, 'left', 'orange')]
        self.assertEqual(answer, solution.sock_match(input))
    def test_expected_nosock(self):
        "Should return no matched socks if there are none."
        solution = Solution()
        answer = []
        input = [(1, 'left', 'red'), (2, 'left', 'orange'), (3, 'left', 'orange')]
        self.assertEqual(answer, solution.sock_match(input))
