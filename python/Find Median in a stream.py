def __init__(self):
        self.g = []
        self.s = []
        
    def balanceHeaps(self):
        if len(self.s) > len(self.g):
            ele = -1 * heappop(self.s)
            heappush(self.g, ele)
        if len(self.s) < len(self.g):
            ele = heappop(self.g)
            heappush(self.s, -1 * ele)
            
    def getMedian(self):
        if len(self.g)<len(self.s):
            return -1*self.s[0]
        else:
            return (self.g[0]-self.s[0])/2
        
    def insertHeaps(self,x):
        heappush(self.s, -1 * x)
        if self.s and self.g and (-1*self.s[0]) > self.g[0]:
            ele = -1 * heappop(self.s)
            heappush(self.g,ele)
        self.balanceHeaps() 
