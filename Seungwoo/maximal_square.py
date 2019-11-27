class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        size = len(matrix[0])
        padded_input = [[0]*(size+1)] + [[0] + l for l in matrix]
        res = 0

        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if matrix[i][j] == "1":
                    padded_input[i+1][j+1] = min(\
                        padded_input[i][j+1], 
                        padded_input[i+1][j], 
                        padded_input[i][j]) + 1
                    if res < padded_input[i+1][j+1]:
                        res = padded_input[i+1][j+1]
                else:
                    padded_input[i+1][j+1] = 0

        return res**2