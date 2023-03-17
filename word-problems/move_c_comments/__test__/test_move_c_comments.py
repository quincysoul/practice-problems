import unittest
from move_c_comments.move_c_comments import Solution


class Test(unittest.TestCase):
    def test_remove_c_comments_1(self):
        "Should remove all comments from code."
        solution = Solution()
        input_str = r"""
        /*.source code../*..comment.*/
        """
        expected = r"""
        /*.source code..
        """
        self.assertEqual(expected, solution.move_c_comments(input_str))

    def test_remove_c_comments_2(self):
        "Should remove all comments from code."
        solution = Solution()
        input_str = r"""
        /*.comment*/...code*/..../*.comment...*/
        """
        expected = r"""
        ...code*/....
        """
        self.assertEqual(expected, solution.move_c_comments(input_str))

    def test_remove_c_comments_3(self):
        "Should remove all comments from code."
        solution = Solution()
        input_str = r"""
        int c1='/*.code*/'/*.comment*/...code*/..../*.comment...*/
        char* p = "/*.code*/";
        /*.comment
            int c1 = '/*.code*/';
            char* p = "/*.code*/";
            'c';
        */
        """
        expected = r"""
        int c1='/*.code*/'...code*/....
        char* p = "/*.code*/";
        
        """
        print("expected:", expected)
        print("act:", solution.move_c_comments(input_str))
        self.assertEqual(expected, solution.move_c_comments(input_str))
