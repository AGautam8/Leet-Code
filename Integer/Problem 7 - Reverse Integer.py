# This solution is for reversing the intger.

class Solution:
    def reverse(self, x: int) -> int:        
        new_num = 0
        d = abs(x)
        while d:            
            d,m = divmod(d,10)
            new_num = (new_num * 10) + m            
        if new_num > 2**31 -1:
            return 0        
        if x >= 0:
            return new_num
        else:
            return new_num * -1