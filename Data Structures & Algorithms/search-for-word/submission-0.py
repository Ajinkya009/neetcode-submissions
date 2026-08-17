class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        rows = len(board)
        cols = len(board[0])

        def helper(r,c,index):
            if index>=len(word):
                return True
            if r<0 or r>=rows or c<0 or c>=cols:
                return False
            if board[r][c]!=word[index]:
                return False
            if (r,c) in visited:
                return False
            visited.add((r,c))
            found = (
                helper(r-1,c,index+1) or 
                helper(r+1,c,index+1) or 
                helper(r,c-1,index+1) or
                helper(r,c+1,index+1))
            visited.remove((r,c))
            return found
        
        for r in range(rows):
            for c in range(cols):
                if helper(r,c,0):
                    return True
        return False
