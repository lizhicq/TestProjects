class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        self.sum = [[0 for j in range(n+1)]
                       for i in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                self.sum[i][j] = matrix[i-1][j-1] + self.sum[i][j-1] + self.sum[i-1][j] - self.sum[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        return self.sum[row2+1][col2+1] - self.sum[row1][col2+1] - self.sum[row2+1][col1] + self.sum[row1][col1]