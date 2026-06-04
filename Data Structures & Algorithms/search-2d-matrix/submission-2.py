class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)) :
            l, r = 0, len(matrix[i]) - 1
            while l <= r :
                m = l + ((r - l) // 2)
                print(i,m)
                if matrix[i][m] == target:
                    return True
                elif matrix[i][m] > target:
                    r = m - 1
                else :
                    l = m + 1
        return False
                
                