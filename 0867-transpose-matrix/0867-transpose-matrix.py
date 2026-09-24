class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        R = len(matrix)
        C = len(matrix[0])

        result = []
        for col in range(C):
            new_row = []
            for row in range(R):
                new_row.append(matrix[row][col])
            result.append(new_row)

        return result