input_file = open("/content/input2_2.txt",'r')
output_file = open("output2_2.txt", 'w')

l1 = input_file.readline()
list1 = input_file.readline().split()
l2 = input_file.readline()
list2 = input_file.readline().split()

n_list = []
if l1 < l2:
    min_1 = l1
else:
    min_1 = l2
i = 0
k = 0
while(i < int(min_1) and k < int(min_1)):
    if int(list1[i]) <= int(list2[k]):
        n_list.append(list1[i])
        i+=1
    else:
        n_list.append(list2[k])
        k+=1       
if i == int(min_1):
    n_list = n_list + list2[k:]  
if k == int(min_1):
    n_list = n_list + list1[i:] 
output_file.write(str(n_list))