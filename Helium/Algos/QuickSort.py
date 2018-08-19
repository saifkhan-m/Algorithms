'''
Created on Feb 18, 2018

@author: hp
'''

class QuickSort(object):
    


    def __init__(self,lst):
        self.lst=lst
         
    def quicksort(self,lst,low,high):
        
        if(low<high):
            pi=self.partition(lst,low,high)
            
            self.quicksort(lst,low,pi-1)
            self.quicksort(low,pi+1,high)
        
    def partition(self,lst,low,high):
        lst=self.lst
        pivot=lst[low]
        i=low
        for j in range(low+1,high+1):
            if(lst[j]<=pivot):
                i+=1
                lst[i],lst[j]=lst[j],lst[i]
        
        lst[low],lst[i]=lst[i],lst[low]
        return i
            
        
        