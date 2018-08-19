'''
Created on Jan 31, 2018

@author: hp
'''


class InsertionSort(object):
    '''
    classdocs
    '''


    def __init__(self,arr):
        '''
        Constructor
        '''
        self.arr=arr
       
         
    
    #insertion sort is implemented
    def insertionsort(self):
        arr=self.arr
        for i in range (1,arr.__len__()):
            key=arr[i]
            j=i-1
            while (j>=0 and arr[j]>key):
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key
            
        return arr


                
        
            