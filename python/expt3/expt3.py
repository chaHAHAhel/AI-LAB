from math import gcd

j1 = int(input("Enter the size of jug 1: "))
j2 = int(input("Enter the size of jug 2: "))
r = int(input("Enter the required quantity in liters: "))

if (r > j1 and r > j2) or r % gcd(j1, j2) != 0:
    print("Solution not possible")
    exit()


def rule1(jug1, jug2):  
    return j1, jug2

def rule2(jug1, jug2):  
    return jug1, j2

def rule3(jug1, jug2):  
    return 0, jug2

def rule4(jug1, jug2):  
    return jug1, 0

def rule5(jug1, jug2):  
    transfer = min(jug1, j2 - jug2)
    return jug1 - transfer, jug2 + transfer

def rule6(jug1, jug2):  
    transfer = min(jug2, j1 - jug1)
    return jug1 + transfer, jug2 - transfer

rules = [rule1, rule2, rule3, rule4, rule5, rule6]

solutions = []

# Stack: (jug1, jug2, path, visited_set)
stack = [(0, 0, [], set())]

while stack:
    jug1_curr, jug2_curr, path, visited = stack.pop()

    path = path + [(jug1_curr, jug2_curr)]
    visited = visited.copy()
    visited.add((jug1_curr, jug2_curr))

    if jug1_curr == r or jug2_curr == r:
        solutions.append(path)
        continue

    for rule in rules:
        next_j1, next_j2 = rule(jug1_curr, jug2_curr)

        if (next_j1, next_j2) not in visited:
            stack.append((next_j1, next_j2, path, visited))


if solutions:
    print("\nAll Possible Solution Paths:\n")
    for i, sol in enumerate(solutions, 1):
        print(f"Solution {i}:")
        for step in sol:
            print(step)
        print()
else:
    print("No solution found.")