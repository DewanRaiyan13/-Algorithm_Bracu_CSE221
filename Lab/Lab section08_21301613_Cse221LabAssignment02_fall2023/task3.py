data = open('input3.txt','r')
result = open('output3.txt','a') 
size = int(data.readline())
start_time =[]
end_time = []
for _ in range(size):
   startTime, endTime = data.readline().split(' ')
   start_time.append(int(startTime))
   end_time.append(int(endTime))  
for i in range(len(start_time)):
   min_loc = i
   for j in range(i+1, len(start_time)):
     if end_time[j] < end_time [min_loc]:
      min_loc = j 
   end_time[i],end_time[min_loc] = end_time[min_loc],end_time[i]  
   start_time[i],start_time[min_loc] = start_time[min_loc],start_time[i]
final= []
final.append ((start_time [0], end_time [0]))
i = 0
j= 1 
count=1 
while j < len(start_time): 
  if start_time[j] >= end_time[i]:
      count+=1
      final.append ((start_time [j], end_time[j]))
      i=j
      j+=1
  else:
      j+=1
result.write(f" {count}\n")
for i in final:
    result.write(f"{i[0]} {i[1]}\n")
result.close()
print(final)