# id =[7, 4, 9 ,3, 2,5, 1]
# marks = [40 ,50, 50, 20 ,10, 10 ,10]

data = open('LAB 1/input3.txt','r')
file = open('output3.txt','a')

length = int(data.readline())

id_str = data.readline().split(' ')
mark_str = data.readline().split(' ') 

id = [int(i) for i in id_str]
marks = [int(i) for i in mark_str]



for i in range(len(id)):
    minloc = i 
    for j in range(i+1,len(id)):
        if marks[j] > marks[minloc]:
            minloc = j 
    marks[i], marks[minloc] = marks[minloc], marks[i]
    id[i], id[minloc] = id[minloc], id[i]

for i in range(len(id)):
    minloc = i 
    for j in range(i+1,len(id)):
        if id[j] < id[minloc] and marks[i]==marks[j] :
            minloc = j 
    id[i], id[minloc] = id[minloc], id[i]

for i in range(length):
    file.write(f"ID: {id[i]} Mark: {marks[i]}\n")


file.close()
