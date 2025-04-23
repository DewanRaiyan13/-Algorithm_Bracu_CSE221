inputfile = open("./input1b.txt", "r")
filelist= inputfile.readlines()
total, sum = filelist[0].split(" ")
total = int(total)
sum = int(sum)

line = filelist[1].split(" ")
new = []
for i in line:
    new.append(int(i))
output = open("Output1b.txt", "a")
i= 0
j= len(new)-1
flag = False
for i in range(len(new)-1, -1, -1):
    if i != j:
        if new[i] + new[j] == sum:
            output.writelines(f"{i+1} {j+1}")
            flag = True
            break
        else:
            if new[i] + new[j]< sum:
                i += 1
            else:
                j -= 1
if flag == False:
    output.writelines("IMPOSSIBLE")
output.close()