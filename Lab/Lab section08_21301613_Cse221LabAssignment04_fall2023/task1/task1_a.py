# -*- coding: utf-8 -*-
"""tasl1-a.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jh3ZJVxPiF-3_9OtTktWKVlN0wmgmHpF
"""

#task1
input=open("/content/sample_data/input-1(A)","r")
n,m=map(int,input.readline().split())
size=n+1
adj=[[0]*size for i in range(size)]
for i in range(m):
  x,y,z=map(int,input.readline().split())
  adj[x][y]=z

with open("/content/sample_data/output-1(A)","w") as output:
  for row in adj:
    output.write(" ".join(map(str,row))+'\n')

