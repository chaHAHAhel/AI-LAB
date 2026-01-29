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
            #this loop(👇) is used to optimize the order of traversal and prevent repeating nodes
            if neighbour not in visited:    
                stack.append(neighbour)

    return result

graph=input_graph()
a=input("enter the starting node: ")
print(dfs(graph,a))