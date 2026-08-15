class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
  
        def helper_fun(current,left_count,right_count):
            if len(current)==2*n:
                output.append(''.join(current))
                return
            if left_count<n:
                current.append("(")
                helper_fun(current,left_count+1,right_count)
                current.pop()
            if right_count<left_count:
                current.append(")")
                helper_fun(current,left_count,right_count+1)
                current.pop()
        helper_fun([],0,0)
        return output