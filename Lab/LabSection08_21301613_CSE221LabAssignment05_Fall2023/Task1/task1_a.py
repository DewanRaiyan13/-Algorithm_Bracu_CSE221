file = open('LAB 5/input1_a.txt','r')
result = open('output1_a.txt','w')


graph_info = file.readline().split(' ')
vertices = int(graph_info[0])
edges = int(graph_info[1])

graph = {} 



for _ in range(edges):
    v_f,v_t = file.readline().split(' ')
    v_f = int(v_f)
    v_t = int(v_t)

    if v_f not in graph:
        graph[v_f] = [v_t]
    else:
        graph[v_f].append(v_t)

cylic = False

color = {v:'white' for v in range(vertices+1)}
def cycle_check():
   
    for v in graph:
        if color[v] == 'white':
            DFS_cycle_check_visit(v)


def DFS_cycle_check_visit(v):
    global cylic
    
    color[v] = "grey"
    if v in graph:   
        for neighbor in graph[v]:
            if  color[neighbor] == "grey":
                cylic = True

            if  color[neighbor] == "white":
                
                DFS_cycle_check_visit(neighbor)
    color[v] = 'black'
    

cycle_check()

if cylic:
    result.write("IMPOSSIBLE")
else:
    
    sorted_list =[]
    visited = {v:0 for v in range(vertices+1)}


    def topological_sort():
        
        
        for v in graph:
            if visited[v] ==0:
                DFS_visit(v)


        
    def DFS_visit(v):
    
        visited[v] = 1
        if v in graph:
            for neighbor in graph[v]:
                if visited[neighbor] == 0:
                    DFS_visit(neighbor)
        sorted_list.insert(0,v)
    topological_sort()

    for i in sorted_list:
        result.write(f"{i} ")




