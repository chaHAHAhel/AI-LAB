from collections import deque
from math import gcd

# Inputs
j1 = int(input("Enter the size of jug 1: "))
j2 = int(input("Enter the size of jug 2: "))
r = int(input("Enter the required quantity in liters: "))

jug1 = 0
jug2 = 0

# Check if solution is possible
if (r > j1 and r > j2) or r % gcd(j1, j2) != 0:
    print("Solution not possible")
    exit()

# Rules (possible moves)
def rule1(jug1, jug2):  # Fill jug1
    return j1, jug2

def rule2(jug1, jug2):  # Fill jug2
    return jug1, j2

def rule3(jug1, jug2):  # Empty jug1
    return 0, jug2

def rule4(jug1, jug2):  # Empty jug2
    return jug1, 0

def rule5(jug1, jug2):  # Pour jug1 → jug2
    transfer = min(jug1, j2 - jug2)
    return jug1 - transfer, jug2 + transfer

def rule6(jug1, jug2):  # Pour jug2 → jug1
    transfer = min(jug2, j1 - jug1)
    return jug1 + transfer, jug2 - transfer

rules = [rule1, rule2, rule3, rule4, rule5, rule6]

# BFS
visited = set()
queue = deque()
queue.append((0, 0, []))  # (jug1, jug2, path)

while queue:
    x, y, path = queue.popleft()

    if (x, y) in visited:
        continue
    visited.add((x, y))
    path = path + [(x, y)]

    # Check goal
    if x == r or y == r:
        print("\nSolution Steps:")
        for step in path:
            print(step)
        break

    # Apply all rules
    for rl in rules:
        nx, ny = rl(x, y)
        if (nx, ny) not in visited:
            queue.append((nx, ny, path))
