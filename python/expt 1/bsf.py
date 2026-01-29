from collections import deque


def input_graph():
    graph={}
    n=int(input("enter the number of nodes: "))
    for _ in range(n):
        node=input("enter the node: ")
        neighbours=input("enter the neighbouring nodes sepeeated by space (press enter if no neighbour): ").split()
        graph[node]=neighbours
    return graph

# graph ={
#     'A': ['B','C','D'],
#     'B': ['E'],
#     'C': ['F'],
#     'D': ['G'],
#     'E': [],
#     'F': ['D'],
#     'G': []
# }

def bfs(graph,start):
    visited =set()
    queue = deque([start])
    result = []
    
    while queue:
        node=queue.popleft()
        if node not in visited:
            result.append(node)
            visited.add(node)
        
        for neigbour in graph[node]:
            if neigbour not in visited:
                visited.add(node)
                queue.append(neigbour)
    
    return result

graph=input_graph()
a=input("enter the starting node: ")
print(bfs(graph,a))
            

