
def rule1(mi,ca,bo):  
    return mi+1,ca,"l"

def rule2(mi,ca,bo):  
    return mi+2,ca,"l"

def rule3(mi,ca,bo):  
    return mi,ca+1,"l"

def rule4(mi,ca,bo):  
    return mi,ca+2,"l"

def rule5(mi,ca,bo):  
    return mi+1,ca+1,"l"
    
def rule6(mi,ca,bo):  
    if bo=="l":
        return mi-1,ca,"r"

def rule7(mi,ca,bo):  
    if bo=="l":
        return mi-2,ca,"r"

def rule8(mi,ca,bo):  
    if bo=="l":
        return mi,ca-1,"r"

def rule9(mi,ca,bo):  
    if bo=="l":
        return mi,ca-2,"r"

def rule10(mi,ca,bo):  
    if bo=="l":
        return mi-1,ca-1,"r"

rulesr=[rule1, rule2, rule3, rule4, rule5]
rulesl=[rule6, rule7, rule8, rule9, rule10]


TOTAL = 3
goal = (0,0,"r")

def is_valid(x, y):
    # Boundary check
    if x < 0 or x > TOTAL or y < 0 or y > TOTAL:
        return False

    m_right = TOTAL - x
    c_right = TOTAL - y

    # Missionaries eaten condition
    if (x > 0 and x < y):
        return False
    if (m_right > 0 and m_right < c_right):
        return False

    return True


def dfs_non_recursive():
    stack = []
    visited = set()

    # Initial state
    stack.append((3,3,"l", []))

    while stack:
        x, y, s, path = stack.pop()

        if (x,y,s) in visited:
            continue

        if not is_valid(x,y):
            continue

        visited.add((x,y,s))
        path = path + [(x,y,s)]

        if (x,y,s) == goal:
            print("\nDFS Solution Found:\n")
            for step in path:
                print(step)
            return

        if s == "r":
            for rl in reversed(rulesr):
                result = rl(x,y,s)
                if result is None:
                    continue
                nx, ny, ns = result
                stack.append((nx,ny,ns,path))

        else:
            for rl in reversed(rulesl):
                result = rl(x,y,s)
                if result is None:
                    continue
                nx, ny, ns = result
                stack.append((nx,ny,ns,path))



dfs_non_recursive()