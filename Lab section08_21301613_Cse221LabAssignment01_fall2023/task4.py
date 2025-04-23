# arr = ['ABCD will departure for Mymensingh at 00:30',
# 'DhumketuExpress will departure for Chittagong at 02:30',
# 'SubornoExpress will departure for Chittagong at 14:30',
# 'ABC will departure for Dhaka at 17:30',
# 'ShonarBangla will departure for Dhaka at 12:30',
# 'SubornoExpress will departure for Rajshahi at 14:30',
# 'ABCD will departure for Chittagong at 01:00',
# 'SubornoExpress will departure for Dhaka at 11:30',
# 'ABC will departure for Barisal at 03:00',
# 'PadmaExpress will departure for Chittagong at 20:30',
# 'ABC will departure for Khulna at 03:00',
# 'ABCE will departure for Sylhet at 23:05',
# 'PadmaExpress will departure for Dhaka at 19:30']

data = open('LAB 1/input4.txt','r')
result = open('output4.txt','a')

length = int(data.readline())
arr = data.readlines()
newArr=[]
for info in arr:
    newArr.append(info[0:-1])

trains = []
for st in arr:
    trains.append(st.split(' ')[0])

times = []
for st in arr:
    times.append(st.split(' ')[6])


for i in range(len(arr)):
    minloc = i 
    for j in range(i+1,len(arr)):
        if trains[j] < trains[minloc]:
            minloc = j 
    trains[i], trains[minloc] = trains[minloc], trains[i]
    newArr[i], newArr[minloc] = newArr[minloc], newArr[i]
    times[i], times[minloc] = times[minloc], times[i]



for i in range(len(arr)):
    minloc = i 
    for j in range(i+1,len(arr)):
        if times[j] > times[minloc] and trains[i] == trains[j] :
            minloc = j 
    newArr[i], newArr[minloc] = newArr[minloc], newArr[i]
    



for info in newArr:
    result.write(f"{info}\n")


result.close()