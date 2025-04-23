import heapq
file = open('input2.txt','r')
result = open('output2.txt','w')

v,e = file.readline().split(' ')
vertices = int(v)
edges = int(e)

graph = {}



def add_edges(v_f,v_t,weight):
    if v_f not in graph:
        graph[v_f] = {v_t:weight}
    else:
        graph[v_f][v_t] = weight  

for _ in range(edges):
    v_f,v_t,weight = file.readline().split(' ')
    v_f = int(v_f)
    v_t = int(v_t)
    weight = int(weight)
    add_edges(v_f,v_t,weight)


source_Alice, source_Bob = file.readline().split(' ')
source_Alice = int(source_Alice)
source_Bob = int(source_Bob)

def dijkstra(start,graph):
    Distances= {vertex:float('inf') for vertex in range(1,vertices+1)}
    Distances[start] = 0 
    priority_queue = [(0,start)]                         

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_vertex in graph.keys():
        
            for neighbor_vertex, weight in graph[current_vertex].items():
                distance = current_distance + weight 

                if distance < Distances[neighbor_vertex] :
                    Distances[neighbor_vertex] = distance 
                    heapq.heappush(priority_queue,(distance,neighbor_vertex))


    return Distances

Alice_path = dijkstra(source_Alice,graph)
Bob_path = dijkstra(source_Bob,graph)


dic= {}
for k in range(1,len(Alice_path)):
    if Alice_path[k]!=float('inf') and Bob_path[k]!= float('inf'):
        highest = max(Alice_path[k],Bob_path[k])
        dic[k] = highest 

t = float('inf') 
n = float('inf')
for node,time in dic.items():
    if time < t:
        t = time 
        n = node 

if t==float('inf') and n==float('inf'):
    result.write(f"Impossible")
else:
    result.write(f"Time {t}\nNode {n}")




