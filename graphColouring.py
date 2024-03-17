def isValid(color, adjList, node, assignments):
    for adjNode in adjList[node]:
        if adjNode < node:
            if assignments[adjNode] == color:
                return False
    
    return True

def dfs(node, adjList, domains, assignments, V):
    if node == V:
        return True
    
    for color in domains[node]:
        if isValid(color, adjList, node, assignments):
            assignments[node] = color
            if dfs(node + 1, adjList, domains, assignments, V):
                return True
            assignments.pop(node)

    return False

def leastDec(node, adjList, domains, assignments, tried):
    mini = (10 ** 7)
    minColor = -1
    for color in domains[node]:
        if color in tried:
            continue
        c = 0
        for adjNode in adjList[node]:
            if adjNode in assignments.keys() and assignments[adjNode] == color:
                c = (10 ** 7)
            elif color in domains[adjNode]:
                c +=1 
        if c < mini:
            mini = c
            minColor = color
    if mini == (10 ** 7):
        return -1
    return minColor
            
def minConflict(node, adjList, domains, assignments, V):
    if node == V:
        return True
    
    tried = set()
    while len(domains[node]) != 0:
        best = leastDec(node, adjList, domains, assignments, tried)
        if best == -1:
            return False
        assignments[node] = best
        if minConflict(node + 1, adjList, domains, assignments, V):
            return True
        tried.add(best)
    
    return False

def check(color, node, adjList, domains, V):
    newDomain = [set() for i in range(V)]

    for adjNode in adjList[node]:
        temp = domains[adjNode]
        if color in temp:
            temp.remove(color)
        if len(temp) == 0:
            return (False, [])
        newDomain[adjNode] = temp
    
    for i in range(V):
        if len(newDomain[i]) == 0:
            newDomain[i] = domains[i]
    
    return (True, newDomain)
    
def forwardCheck(node, adjList, domains, assignments, V):
    if node == V:
        return True

    for color in domains[node]:
        result, newDomain = check(color, node, adjList, domains, V)
        if result == False: continue
        assignments[node] = color
        if forwardCheck(node + 1, adjList, newDomain, assignments, V):
            return True
        assignments.pop(node)

    return False

def checkArc(node, adjList, domains, color, V):
    newDomains = []
    for i in range(V):
        if i == node:
            temp = set()
            temp.add(color)
            newDomains.append(temp)
        else:
            newDomains.append(domains[i])
        
    q = [] # for every value in left do we have a value in right
    for adjNode in adjList[node]:
        q.append((node, adjNode))
        q.append((adjNode, node))
    
    
    while q:
        left, right = q.pop(0)
        tempDomain = newDomains[left]
        for color in tempDomain:
            if color in newDomains[right] and len(newDomains[right]) == 1:
                newDomains[left].remove(color)
                if len(newDomains[left]) == 0:
                    return (False,[])
                for adjNode in adjList[node]:
                    q.append((adjNode, node))
    
    return (True, newDomains)



def arcChecking(node, adjList, domains, assignments, V):
    if node == V:
        return True
    
    for color in domains[node]:
        result, newDomains =  checkArc(node, adjList, domains, color, V)
        if result == False: return False
        assignments[node] = color
        if arcChecking(node + 1, adjList, newDomains, assignments, V):
            return True
        assignments.pop(node)
    
    return False
        
def arcConsistency(adjList, domains, V):
    assignments = {}
    k = arcChecking(0, adjList, domains, assignments, V)
    return assignments

def forwardChecking(adjList, domains, V):
    assignments = {}
    k = forwardCheck(0, adjList, domains, assignments, V)
    return assignments

def minimumConflict(adjList, domains, V):
    assignments = {}
    k = minConflict(0, adjList, domains, assignments, V)
    return assignments

def backtracking(adjList, domains, V):
    assignments = {}
    k = dfs(0, adjList, domains, assignments, V)
    return assignments

if __name__ == "__main__":
    V = 7

    # wa - 0, nt - 1, q - 2, nsw - 3, v - 4, sa - 5 , t - 6
    adjList = [[1, 5], [0, 5, 2], [1, 5, 3], [6, 5, 2], [3, 5], [0, 1, 3, 2, 4, 6], []]

    #r - 0, g - 1, b - 2
    domains = []
    for i in range(V):
        temp = set()
        for j in range(3):
            temp.add(j)
        domains.append(temp)

    assignments = backtracking(adjList, domains, V)
    print(assignments)
    assignments = minimumConflict(adjList, domains, V)
    print(assignments)
    assignments = forwardChecking(adjList, domains, V)
    print(assignments)
    assignments = arcConsistency(adjList, domains, V)
    print(assignments)
