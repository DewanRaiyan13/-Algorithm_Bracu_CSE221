data = open('input3.txt','r')
N,K = map(int,data.readline().split())

result = open('output3.txt','w')

dset = []

for i in range(1,N+1):
    dset.append([i])

for q in range(K):
    a,b = map(int,data.readline().split())
    for i in range(len(dset)):
        if a in dset[i] and b not in dset[i]:
            for j in range(len(dset)):
                if b in dset[j] and a not in dset[j]:
                    dset[i].extend(dset[j])
                    result.write(str(len(dset[i]))+'\n')
                    dset[j] = []
                    break
