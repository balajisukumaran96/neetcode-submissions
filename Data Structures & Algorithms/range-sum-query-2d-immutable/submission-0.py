class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        if not matrix or not matrix[0]:
            return

        n = len(matrix)
        m = len(matrix[0])
        self.prefixSum = [[0] * (m+1) for _ in range(n+1)]

        for i in range(n):
            for j in range(m):
                self.prefixSum[i+1][j+1] = (matrix[i][j] - self.prefixSum[i][j] + self.prefixSum[i][j+1] + self.prefixSum[i+1][j])

          
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        full = self.prefixSum[row2+1][col2+1]
        corner = self.prefixSum[row1][col1]
        top = self.prefixSum[row1][col2+1]
        left = self.prefixSum[row2+1][col1]
        return full - top - left + corner 
    

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)