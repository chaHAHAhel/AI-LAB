from collections import deque

graph ={
    'A': ['B','C','D'],
    'B': ['E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['D'],
    'G': []
}

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

print(bfs(graph,'A'))
            

