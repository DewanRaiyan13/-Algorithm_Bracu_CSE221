
file_open = open("./input1a.txt", "r")
fileInList = file_open.readlines()
total, sum = fileInList[0].split(" ")
total = int(total)
sum = int(sum)
line = fileInList[1].split(" ")
new = []
for i in line:
    new.append(int(i))
output = open("Output1a.txt", "a")

for i in range(len(new)):
    for j in range(len(new)-1, i, -1):
        if new[i] + new[j] == sum:
            output.writelines(f"{i+1} {j+1}")
output.close()
