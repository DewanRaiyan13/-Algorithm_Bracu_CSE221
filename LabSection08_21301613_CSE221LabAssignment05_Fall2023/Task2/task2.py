import heapq
file = open('input2.txt','r')
result = open('output2.txt','w')

graph_info = file.readline().split(' ')
vertices = int(graph_info[0])
edges = int(graph_info[1])

graph = {}

def add_edges(v_f,v_t):
    v_f = int(v_f)
    v_t = int(v_t)
    if v_f not in graph:
        graph[v_f] = [v_t]
    else:
        graph[v_f].append(v_t)

for _ in range(edges):
    v_f,v_t = file.readline().split(' ')
    add_edges(v_f,v_t)





def topological_sort():
    priority_q = []
    in_degree = {v:0 for v in range(1,vertices+1)}
    for v in graph:
        for neihbor in graph[v]:
            if neihbor not in in_degree:
                in_degree[neihbor] = 0 
            else:
                in_degree[neihbor]+=1 
    
    sorted_list =[]
    for v in in_degree:
        if in_degree[v] == 0:
            heapq.heappush(priority_q,v)


    while priority_q:
        v = heapq.heappop(priority_q)
        sorted_list.append(v)
        if v in graph:
            for neighbor in graph[v]:
                in_degree[neighbor] -= 1 
                if in_degree[neighbor] == 0:
                    heapq.heappush(priority_q,neighbor)


    if len(sorted_list)!= vertices:
        result.write("IMPOSSIBLE")

    else:
        for i in sorted_list:
            result.write(f"{i} ")


topological_sort()


