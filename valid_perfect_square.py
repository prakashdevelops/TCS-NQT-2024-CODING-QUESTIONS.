class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        s=num**0.5
        if s*s==num and int(s)==s:
            return True
        else:
            return False
