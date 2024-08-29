class Solution:
    def addDigits(self, num: int) -> int:
        s=str(num)
        a=[]
        for i in range(0,len(s)):
            a.append(int(s[i]))
        k=sum(a)
        if k<10:
            return k
        else:
            return self.addDigits(k)      
