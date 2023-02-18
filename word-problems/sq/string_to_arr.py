"""[summary]
Problem: Given binary string fill in the R x C matrix with the characters...
R = 4
C = 4
...

Time Complexity: [O (R * C)]
    1. 
Space Complexity: [O (R * C)]
    * 
Returns:
    Matrix of R * C
"""
class Solution:
    def string_to_arr(self, bin_string, R, C) -> bool:
        matrix = [
            [
                0 for _ in range(C)
            ] for _ in range(R)
        ]

        k = 0
        for i, row in enumerate(matrix):
            for j, col in enumerate(matrix[i]):
                matrix[i][j] = int(bin_string[k])
                k += 1
        
        return matrix