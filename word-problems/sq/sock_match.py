"""[summary]
Problem: Match left and right socks of the same color.
Given an array like [(1, 'left', 'red'), (2, 'right', 'red'), (3, 'left', 'orange')]
Pair 0,1.

Time Complexity: [O
    1. 
Space Complexity: [O
    * 
Returns:
    List of pairs of same color socks.
"""


class Solution:
    def sock_match(self, input_socks: list) -> list:
        res = []
        seen = {}
        for id_num, side, color in input_socks:
            if side == 'left' and seen.get(color, {}).get('side', False) == 'right':
                    res.append((id_num, seen[color]['id_num'], color))
                    del seen[color]
            elif side == 'right' and seen.get(color, {}).get('side', False) == 'left':
                    res.append((id_num, seen[color]['id_num'], color))
                    del seen[color]
            else:
                seen[color] = {'id_num': id_num, 'side': side}
        return res