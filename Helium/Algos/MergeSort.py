from math import floor
class MergeSort(object):
    '''
    classdocs
    '''


    def __init__(self, arr):
        '''
        Constructor
        '''
        self.arr=arr
        
    def MergeSort(self,start,end):
        #arr=self.arr
        if(start<end):
            mid=floor((start+(end-1))/2)
            self.MergeSort(start, mid)
            self.MergeSort(mid+1, end)
            self.merge(start,mid,end)
    
    def merge(self,p,q,r):
        arr=self.arr
        n1=q-p+1
        n2=r-q
        
        Left=[None]*(n1)
        print(Left)
        Right=[0]*(n2)
        for i in range(0,n1):
            Left[i]=arr[p+i]
        
        for j in range(0,n2):
            Right[j]=arr[q+1+j]
        
        
        i=0
        j=0
        k=p
        while(i<n1 and j<n2):
            if(Left[i]<Right[j]):
                arr[k]=Left[i]
                i+=1
            else:
                arr[k]=Right[j]
                j+=1
            
            k+=1
        
        
         
        while i<n1:
            arr[k]=Left[i]
            i+=1
            k+=1
        
        while j<n2:
            arr[k]=Right[j]
            j+=1
            k+=1
        
        
            
        
        
        