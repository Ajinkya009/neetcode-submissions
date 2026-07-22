class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = "".join(s.split(' '))
        print(t)
        l,r = 0,len(t)-1
        while l<r:
            while l<r and not t[l].isalnum():
                l+=1
            while l<r and not t[r].isalnum():
                r-=1
            if t[l].lower()!=t[r].lower():
                return False
            l+=1
            r-=1
        return True