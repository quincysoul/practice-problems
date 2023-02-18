class Solution:
    def sequence_points(self, sequence_list):
        points = 0
        sequence_list.sort(key=self.custom_sort)

        end_point = sequence_list[0][1]

        i = 0
        while i < len(sequence_list):
            print("sequence_list[i]", sequence_list[i])

            if end_point >= sequence_list[i][0]:
                pass
            else:
                points += 1
                end_point = sequence_list[i][1]
            i += 1

        return points + 1

    def custom_sort(self, sequence):
        return sequence[1], sequence[0]


solution = Solution()
print(
    "should return 3",
    solution.sequence_points(
        [[-1, 3], [-5, -3], [3, 5], [2, 4], [-3, -2], [-1, 4], [5, 5]]
    ),
)

print("should return 2", solution.sequence_points([[10, 16], [2, 8], [1, 6], [7, 12]]))
