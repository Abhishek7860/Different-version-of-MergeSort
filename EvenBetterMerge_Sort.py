# Program to perform the merge sort by creating auxiliary array. Data alternate between A and B and the final sorted array is defined by height value.
# This program is done in python 3.4
# UTD ID : 2021206862 ; Abhishek Kumar
"""
A = List to be sorted
p = starting of the array
q = mid of the array
r = End point of the array
B  = Auxiliary list to perform swapping and can contain the final sorted array as per the height value
"""
import time
def MergeSort(A,p,r,B):
    if (p>=r):
        return 0
    else:
        q = int((p+r)/2)
        h1 = MergeSort(A,p,q,B)#recursive call of merge sort for left part of list
        h2 = MergeSort(A,q+1,r,B)#recursive call of merge sort for right part of list
        if h1 != h2:
            print("Not power of two")
            exit();# Terminates the program if the heights doesnt match
        else :
            if int(h1 % 2) == 1 :
                Merge(B,p,q,r,A)# If h1 (height) is odd the resultant array will be A
            else:
                Merge(A,p,q,r,B)# If h1 (height) is odd the resultant array will be A
        return h1+1          

def Merge(A,p,q,r,B): #Function to perform comparision and swapping of elements and storing it back to the array
    k=p
    j=q+1
    for i in range(p,r+1,1): # i from p to r+1
        if j> r or (k<= q and A[k]<=A[j]):
            B[i]= A[k]
            k=k+1
        else:
             B[i]=A[j]
             j=j+1
      
A = []
array_size = input("enter the array size : ")
for i in range(1,int(array_size)+1):
    A.append(i)# filling the array
A.reverse()# reversing the original array
leng = len(A)-1
B = [0]*len(A)# initializing the list B of same size of A and initializing the value of each elment of B with 0
print(A)
start_time = time.time()
final=MergeSort(A,0,leng,B)# final has the value which will help us know which array has the sorted array
elapsed_time = time.time()
if final%2 == 0 :
    print ("Sucess")# Put A (in print)to print the sorted array
else :
    print ("Sucess")# Put B (in print)to print the sorted array
print("Time Elapsed : ",(elapsed_time - start_time)*1000, "Milliseconds")
