from math import gcd

# Inputs
j1 = int(input("Enter the size of jug 1: "))
j2 = int(input("Enter the size of jug 2: "))
r = int(input("Enter the required quantity in liters: "))

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

solutions = []

def dfs(jug1, jug2, path, visited):
    # Add current state
    path.append((jug1, jug2))
    visited.add((jug1, jug2))

    # If solution found
    if jug1 == r or jug2 == r:
        solutions.append(path.copy())
    else:
        for rule in rules:
            next_j1, next_j2 = rule(jug1, jug2)

            if (next_j1, next_j2) not in visited:
                dfs(next_j1, next_j2, path, visited)

    # Backtrack
    path.pop()
    visited.remove((jug1, jug2))

# Start DFS from (0,0)
dfs(0, 0, [], set())

# Print all solutions
if solutions:
    print("\nAll Possible Solution Paths:\n")
    for i, sol in enumerate(solutions, 1):
        print(f"Solution {i}:")
        for step in sol:
            print(step)
        print()
else:
    print("No solution found.")