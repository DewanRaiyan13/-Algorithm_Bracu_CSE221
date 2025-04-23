file = open('LAB 1/input1b.txt','r')
line = file.readline()
f = open("output1b.txt", "a")

for i in range(int(line)):
  line = file.readline()
  n1 = int(line.split(' ')[1])
  sign = line.split(' ')[2]
  n2 =  int(line.split(' ')[3])

  if sign == '+':
    res = n1+n2
    f.write(f'The result of {n1} {sign} {n2} is {res} \n')
  elif sign == '*':
    res = n1*n2
    f.write(f'The result of {n1} {sign} {n2} is {res} \n')
  if sign == '-':
    res = n1-n2
    f.write(f'The result of {n1} {sign} {n2} is {res} \n')
  if sign == '/':
    res = n1/n2
    f.write(f'The result of {n1} {sign} {n2} is {res} \n')


f.close()
