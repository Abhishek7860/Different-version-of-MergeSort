#Program to perform merge sort with help of two auxiliary list left and right
# This program is done in python 3.4
# UTD ID : 2021206862 ; Abhishek Kumar 
"""
A = List to be sorted
p = starting of the array
q = mid of the array
r = End point of the array
left  = Left part auxiliary array to perform sort
right = Right part auxiliary array to perform sort
"""
import time
left = list()
right = list()
def MergeSort(A,p,r):    
    if (r-p <= 11):
        insertion_sort(A)# calling insertion sort for short list (size less than 11)
    else:
        q = int((p+r)/2)
        MergeSort(A,p,q)#recursive call of merge sort for left part of list
        MergeSort(A,q+1,r)#recursive call of merge sort for right part of list
        Merge(A,p,q,r)
    
def insertion_sort(A):# Insertion sort
    for i in range(1,len(A)):
        temp = A[i]
        j=i
        while(A[j-1]>temp):
            A[j]=A[j-1]
            if(j>0):
                j=j-1
            else:
                break
        A[j]=temp
    
def Merge(A,p,q,r): #Function to perform comparision and merging of two array
    left = list(A[p:q+1])#copying the left part of list A to left
    right = list(A[q+1:r+1])#copying the right part of list A to right
    k=0
    left.append(100*int(array_size))#appending one more element in left with a very high value 
    right.append(100*int(array_size))
    j=0
    for i in range(p,r+1,1):
        if left[k] <= right[j]:
            A[i]= left[k]
            k=k+1
        else:
            A[i]=right[j]
            j=j+1
      
A = []
array_size = input("enter the array size : ")
for i in range(1,int(array_size)+1):
    A.append(i)# filling the array with values
A.reverse()# reversing the original array
leng = len(A)-1
start_time = time.time()
MergeSort(A,0,leng)
elapsed_time = time.time()
print ("Sucess")
print("Time Elapsed : ",((elapsed_time - start_time)*1000), "Milliseconds")


