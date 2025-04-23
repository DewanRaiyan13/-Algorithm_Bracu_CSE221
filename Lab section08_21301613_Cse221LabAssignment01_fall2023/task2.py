data = open('input2.txt','r')

file = open("output2.txt", "a")


length = int(data.readline())

arr_str = data.readline().split()

arr = [int(i) for i in arr_str]

def bubbleSort(arr): 
    flag = False
    for i in range(len(arr)-1):
        
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True 
        if flag == False:
            break
bubbleSort(arr)

file.write(' '.join(str(n) for n in arr))

file.close()


# We use a flag achieved the θ(n) for the best-case scenario. In the inner loop if any value of array get swapped 
# then flag become true which  indicates loop is not sorted. On the other case, if the array is sorted then flag will remain false 
# and it will terminates the outer loop.


