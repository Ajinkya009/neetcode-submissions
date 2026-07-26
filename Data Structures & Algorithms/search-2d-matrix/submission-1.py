class Solution:
    def search(self, matrix,row,num_cols,target):
        left,right = 0,num_cols-1
        while left<=right:
            m = left+ (right-left)//2
            if target==matrix[row][m]:
                return True
            elif target>matrix[row][m]:
                left=m+1
            else:
                right=m-1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows,num_cols = len(matrix),len(matrix[0])

        for i in range(num_rows):
            if target>=matrix[i][0] and target<=matrix[i][num_cols-1]:
                return self.search(matrix,i,num_cols,target)
        return False