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

def dfs(graph,start):
    stack=deque([start])
    result=[]
    visited=set()

    while stack:
        node=stack.pop()

        if node not in visited:
            visited.add(node)
            result.append(node)
        
        for neighbour in reversed(graph[node]):
            #if neighbour not in visited:
           stack.append(neighbour)

    return result

print(dfs(graph,'A'))