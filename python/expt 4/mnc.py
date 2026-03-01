from collections import deque

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
    return mi-1,ca,"r"

def rule7(mi,ca,bo):  
    return mi-2,ca,"r"

def rule8(mi,ca,bo):  
    return mi,ca-1,"r"

def rule9(mi,ca,bo):  
    return mi,ca-2,"r"

def rule10(mi,ca,bo):  
    return mi-1,ca-1,"r"

rulesr=[rule1, rule2, rule3, rule4, rule5]
rulesl=[rule6, rule7, rule8, rule9, rule10]

TOTAL = 3
goal= (0,0,"r")
visited = set()
queue = deque()
queue.append((3, 3, "l", []))

def is_valid(mi, ca):
    # bounds check
    if mi < 0 or mi > TOTAL or ca < 0 or ca > TOTAL:
        return False

    m_right = TOTAL - mi
    c_right = TOTAL - ca

    # missionaries eaten condition
    if (mi > 0 and mi < ca):
        return False
    if (m_right > 0 and m_right < c_right):
        return False

    return True

while queue:
    x, y, s, path = queue.popleft()

    if (x, y, s) in visited:
        continue
    visited.add((x, y, s))

    path = path + [(x, y, s)]

    if (x,y,s) == goal:
        print("\nSolution Steps:")
        for step in path:
            print(step)
        break

    # If boat on RIGHT use rulesr
    if s=="r":
        for rl in rulesr:
            result = rl(x, y, s)
            if result is None:
                continue
            nx, ny, ns = result
            if is_valid(nx, ny) and (nx,ny,ns) not in visited:
                queue.append((nx, ny, ns, path))

    # If boat on LEFT use rulesl
    else:
        for rl in rulesl:
            result = rl(x, y, s)
            if result is None:
                continue
            nx, ny, ns = result
            if is_valid(nx, ny) and (nx,ny,ns) not in visited:
                queue.append((nx, ny, ns, path))