class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows,num_cols = len(matrix),len(matrix[0])
        left,right = 0,num_rows*num_cols-1
        while left<=right:
            m = left + (right-left)//2
            row = m //num_cols
            col = m%num_cols
            if matrix[row][col]<target:
                left = m+1
            elif matrix[row][col]>target:
                right=m-1
            else:
                return True
        return False