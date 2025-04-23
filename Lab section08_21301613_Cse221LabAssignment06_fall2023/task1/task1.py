import heapq
file = open('input1.txt','r')
result = open('output1.txt','w')

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


source = file.readline()
source = int(source)

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




ShortestPath = dijkstra(source,graph)
for k in ShortestPath:
    if ShortestPath[k] == float('inf'):
        result.write(f"-1 ")
    else:
        result.write(f"{ShortestPath[k]} ")
