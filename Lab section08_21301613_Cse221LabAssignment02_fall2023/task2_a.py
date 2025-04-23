input_file=open('input2a.txt','r')
output_file=open('output2a.txt','w')
ip_data= input_file.readlines()
M=int(ip_data[0])
arr1=ip_data[1].split(' ')
N=int(ip_data[2])
arr2=ip_data[3].split(' ')
arr=[]
for i in range(M+N):
    if i<M:
        arr.append(int(arr1[i]))
    else: 
       arr.append(int(arr2[i-M]))
r=M+N
#print(arr)
def MERGE (A, p, q, r ):
    L=A[p:q-p+1]
    R=A[q-p+1:r+1]
    if len(L)==0 or len(R)==0:
        return
    else:
        pass
    i = 0
    j = 0
    for k in range(p,r):
      if i>=len(L) or j>=len(R):
        break
      else:
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
      if k<len(A):
        A[k] = R[j]
        j += 1
        k += 1
      else:
         break
def MERGE_SORT(A, p, r):
    if p < r:
       q = (p+r)//2
       MERGE_SORT (A, p, q)
       MERGE(A, p, q, r)
       MERGE_SORT (A, q+1 , r)
    else:
        return   
MERGE_SORT(arr, 0, r-1)
#print(arr)
for i in arr:
    print(i,end=' ',file=output_file)