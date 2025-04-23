import heapq
file = open('input4.txt','r')
result = open('output4.txt','w')

v,e = file.readline().split(' ')
vertices = int(v)
edges = int(e)

graph = {}


# Making the adjacent list (using Dictionary here) undirected 
def add_edges(v_f,v_t,weight):
    if v_f not in graph:
        graph[v_f] = {v_t:weight}
    else:
        graph[v_f][v_t] = weight  

    if v_t not in graph:
        graph[v_t] = {v_f:weight}
    else:
        graph[v_t][v_f] = weight 
        

for _ in range(edges):
    v_f,v_t,weight = file.readline().split(' ')
    weight = int(weight)
    v_f = int(v_f)
    v_t = int(v_t)
    add_edges(v_f,v_t,weight)

visited = {v:False for v in range(1,vertices+1)}

def prims(start,graph):
    total_weight = 0
    Distances= {vertex:float('inf') for vertex in range(1,vertices+1)}
    visited[start] = True 
    Distances[start] = 0 
    priority_queue = [(weight, start, neighbor) for neighbor, weight in graph[start].items()]      
    heapq.heapify(priority_queue) 
    mst = []
 

    while priority_queue:

        weight, v_f,v_t = heapq.heappop(priority_queue)
        
        if  visited[v_t] == False:
            visited[v_t] = True  
            mst.append((v_f,v_t,weight))
            total_weight += weight 
            if v_t in graph:

                for neighbor_vertex, weight in graph[v_t].items():
                        if weight < Distances[neighbor_vertex]:
                            Distances[neighbor_vertex] = weight 
                            heapq.heappush(priority_queue,(weight,v_t,neighbor_vertex))
       


    return total_weight


source =1


result.write(f'{prims(source,graph)}')









