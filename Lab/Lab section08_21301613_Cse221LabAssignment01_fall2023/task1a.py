file = open('input1a.txt','r')
f = open("output1a.txt", "a")

lines = file.readlines()

numbers = []
for i in lines:
  numbers.append(int(i))

for i in range(numbers[0]):
  if numbers[i+1]%2 == 0:
    f.write(f'{numbers[i+1]} is an even number\n')
  else:
     f.write(f'{numbers[i+1]} is an odd number\n')


f.close()