class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = [b for b in str(x)]
        b = a[::-1]
        if a == b:
            return True
        else:
            return False
            
            
        

