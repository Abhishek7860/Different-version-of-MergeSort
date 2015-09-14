# Program to perform the merge sort by creating auxiliary array and passing to MergeSort and Merge. Data is copied from A to B and merge back to A
# This program is done in python 3.4
# UTD ID : 2021206862 ; Abhishek Kumar
"""
A = List to be sorted
p = starting of the array
q = mid of the array
r = End point of the array
B  = Auxiliary array to perform sort
"""
import time
B = list()

def MergeSort(A,p,r,B):
    if (p>=r):#return if the array has only one element
        return 0
    else:
        q = int((p+r)/2)
        MergeSort(A,p,q,B)#recursive call of merge sort for left part of list
        MergeSort(A,q+1,r,B)#recursive call of merge sort for right part of list
        Merge(A,p,q,r,B)
    

def Merge(A,p,q,r,B): #Function to perform comparision and merging of two array
    ls=q-p+1 #calculating ls and rs to reach out to full range of list
    rs=r-q
    B= A[p:q+1]# copying the element of from A to B 
    B.extend(A[q+1:r+1])
    k=0
    j=ls
    for i in range(p,r+1,1):
        if j>=ls+rs or (k<=ls and B[k]<=B[j]):
            A[i]= B[k]
            k=k+1
        else:
            A[i]=B[j]
            j=j+1
      
A = []
array_size = input("enter the array size : ")
for i in range(1,int(array_size)+1):
    A.append(i)# filling the array
A.reverse()# reversing the original array
leng = len(A)-1
start_time = time.time()
MergeSort(A,0,leng,B)
elapsed_time = time.time()
print("Sucess")
print((elapsed_time - start_time)*1000, "Miliseconds")
