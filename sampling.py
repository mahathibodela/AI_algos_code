import collections
import random

def topoSort(edges, cpt):
    adjList = collections.defaultdict(list)
    indegree = collections.defaultdict(list)
    for i in cpt:
        indegree[i] = 0
    for edge in edges:
        adjList[edge[0]].append(edge[1])
        indegree[edge[1]] += 1
    
    q = []
    for key,value in indegree.items():
        if value == 0:
            q.append(key)
    order = []
    parents =collections.defaultdict(list)
    while q:
        node = q.pop()
        order.append(node)
        for adjNode in adjList[node]:
            parents[adjNode].append(node)
            indegree[adjNode] -= 1
            if indegree[adjNode] == 0:
                q.append(adjNode)
    
    return (order, parents, adjList)

def simpleSample(order, parent, cpt):
    sample = {}
    for node in order:
        prop = random.random()
        if node not in parent:
            sample[node] = prop <= cpt[node]
        else:
            sample[node] = prop <= cpt[node][tuple(sample[parent] for parent in parents[node])]
    return sample

def isValid(evidence, sample):
    for i in evidence:
        if evidence[i] != sample[i]:
            return False
    return True

def isFav(query, sample):
    for i in query:
        if query[i] != sample[i]:
            return False
    return True

def rejectionSampling(order, parent, adjList, cpt, evidence, query):
    favSamples = 0
    totSamples = 0
    n = 1000
    for i in range(n):
        sample = simpleSample(order, parent, cpt)
        if isValid(evidence, sample):
            totSamples += 1
            if isFav(query, sample):
                favSamples += 1
    prop = favSamples/totSamples
    return prop

def weightedSample(order, parent, cpt, evidence):
    sample = {}
    w = 1
    for node in order:
        if node in evidence:
            sample[node] = evidence[node]
            if node not in parent:
                temp = cpt[node]
                if evidence[node] == True:
                    w *= temp
                else: w *= (1 - temp)
            else:
                temp = cpt[node][tuple(sample[parent] for parent in parents[node])]
                if evidence[node] == True:
                    w *= temp
                else: w *= (1 - temp)
        else:
            prop = random.random()
            if node not in parent:
                sample[node] = prop <= cpt[node]
            else:
                sample[node] = prop <= cpt[node][tuple(sample[parent] for parent in parents[node])]
    
    return (sample, w)



def likelihoodWeighting(order, parent, adjList, cpt, evidence, query):
    favWeight = 0
    totWeight = 0
    n = 1000
    for i in range(n):
        sample, w = weightedSample(order, parent, cpt, evidence)
        if isFav(query, sample):
            favWeight += w
        totWeight += w
    prop = favWeight / totWeight
    return prop

def gibbsSampling(order, parents, adjList, cpt, evidence, query):
    sample = {}
    remaining = []
    favSample = 0

    for node in order:
        if node in evidence:
            sample[node] = evidence[node]
        else:
            sample[node] = random.choice([False, True])
            remaining.append(node)
    
    n = 10000
    for i in range(n):
        node = random.choice(remaining)
        if node not in parents:
            prop = cpt[node]
        else:
            prop = cpt[node][tuple([sample[parent] for parent in parents[node]])]
        
        temp = random.random()
        sample[node] = temp <= prop
        if isFav(query, sample):
            favSample += 1
    
    res = favSample / n
    return res

if __name__ == "__main__":
    edges = [['A','B'],['A','C'],['B','C'],['C','D'],['E','D']]
    cpt = {
        "A":0.3,
        "B":{(True,):0.1 , (False,):0.6},
        "C":{(True,True):0.05, (True,False):0.5, (False,True):0.45, (False,False):0.6},
        "E":0.35,
        "D":{(True,True):0.01, (True,False):0.75, (False,True):0.5,(False,False):0.31},
    }

    order, parents, adjList = topoSort(edges, cpt)
    evidence = {'C' : False}
    query = {'A' : True}
    ans = rejectionSampling(order, parents, adjList, cpt, evidence, query)
    print(ans)
    ans = likelihoodWeighting(order, parents, adjList, cpt, evidence, query)
    print(ans)
    ans = gibbsSampling(order, parents, adjList, cpt, evidence, query)
    print(ans)