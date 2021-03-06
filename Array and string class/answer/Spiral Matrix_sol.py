class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # sol 1:
        # res = []
        # if len(matrix)==0: return res
        # rowBegin = 0
        # rowEnd = len(matrix)-1
        # colBegin = 0
        # colEnd = len(matrix[0])-1 
        # while (rowBegin <= rowEnd and colBegin <= colEnd):
        #     # right
        #     for j in range(colBegin, colEnd+1):
        #         res.append(matrix[colBegin][j])
        #     rowBegin+=1
        #     # down
        #     for j in range(rowBegin, rowEnd+1):
        #         res.append(matrix[j][colEnd])
        #     colEnd-=1
        #     # left
        #     if rowBegin <= rowEnd:
        #         for j in range(colEnd, colBegin-1, -1):
        #             res.append(matrix[rowEnd][j])
        #     rowEnd-=1
        #     # up
        #     if colBegin <= colEnd:
        #         for j in range(rowEnd, rowBegin-1, -1):
        #             res.append(matrix[j][colBegin])
        #     colBegin+=1
        # return res
        
        # sol 2:
        res = []
        while True:
            try:
                res += matrix.pop(0)
                for row in matrix:
                    res.append(row.pop())
                res+= matrix.pop()[::-1]
                for row in matrix[::-1]:
                    res.append(row.pop(0))
            except:
                return res 
        return res