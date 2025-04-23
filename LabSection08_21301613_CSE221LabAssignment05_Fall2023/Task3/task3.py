file = open('input3.txt','r')
result = open('output3.txt','w')

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





def transpose_graph():
    trans_graph = {v:[] for v in range(1,vertices+1)}


    for k,v in graph.items():
        for i in v:
            trans_graph[i].append(k)
    return trans_graph
        

def DFS_visit(u,visited,stack):
    visited[u] = 1
    if u in graph:
        for v in graph[u]:
            if visited[v] == 0:
                DFS_visit(v,visited,stack)
    stack.append(u)

def DFS_SCC(u,scc,visited,transposed_Graph):
    visited[u] = 1
    scc.append(u)

    for v in transposed_Graph[u]:
        if visited[v] == 0:
            DFS_SCC(v,scc,visited,transposed_Graph)

    


def strongly_connected_components():
    stack =[]
    visited = {v:0 for v in range(1,vertices+1)}
    for u in graph:
        if visited[u] == 0:
            DFS_visit(u,visited,stack)


    transposed_Graph = transpose_graph()
    visited = {v:0 for v in range(1,vertices+1)}
    All_scc =[]

    while stack:
        u = stack.pop()
        if visited[u] == 0:
            scc=[]
            DFS_SCC(u,scc,visited,transposed_Graph)
            All_scc.append(scc)

    return All_scc 


SCC = strongly_connected_components()

for lst in SCC:
    for i in lst:
        result.write(f"{i} ")
    result.write(f"\n")
   

