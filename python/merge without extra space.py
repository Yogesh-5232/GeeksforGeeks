def merge(self,arr1,arr2,n,m):
        #code here
        arr3=[]
        arr3.extend(arr1)
        arr3.extend(arr2)
        arr3.sort()
        arr1.clear()
        arr2.clear()
        arr1.extend(arr3[:n])
        arr2.extend(arr3[n:])
        return arr1,arr2
