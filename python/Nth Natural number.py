def findNth(self,N):
        #code here
        ans = 0
        mul = 1
        while(N):
            ans += (N%9)*mul
            N//=9
            mul *= 10
        return ans
