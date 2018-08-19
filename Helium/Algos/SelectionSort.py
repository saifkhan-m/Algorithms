'''
Created on Jan 31, 2018

@author: hp
'''

class SelectionSort(object):
    '''
    classdocs
    '''


    def __init__(self,arr):
        '''
        Constructor
        '''
        self.arr=arr
        
    def SelectionSort(self):
        arr=self.arr
        for i in range(0,arr.__len__()):
            for j in range(0,i):
                if(arr[i]<arr[j]):
                    arr[j],arr[i]=arr[i],arr[j]
                
        return arr