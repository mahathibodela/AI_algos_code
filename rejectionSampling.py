import collections
def topologicalSort(adjList, map, V):
    indegree = [0 for i in range(V)]
    q = []

    for adjNodes in adjList:
        for adjNode in adjNodes:
            indegree[adjNode] += 1
    
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)
    
    res = []
    while q!=0:
        node = q.pop(0)
        res.append(node)
        for adjNode in adjList[node]:
            indegree[adjNode] -= 1
            if indegree[adjNode] == 0:
                q.append(adjNode)
    
    return res


def preProcessing(graph):
    variblesMapping = {}
    reverseMapping = {}

    i = 0
    for key in graph.keys():  #variables number
        variblesMapping[key] = i
        reverseMapping[i] = key
        i += 1
    
    V = len(varibleMapping)
    adjList = [[] for i in range(V)]
    for key, items in graph.items(): #adjcency list in numbers is created
        temp = []
        for item in items:
            temp.append(variblesMapping[item])
        adjList[varibleMapping[key]] = temp
    
    order = topologicalSort(adjList, varibleMapping, V) #gives the order in which we have to go
    return (order, variblesMapping, reverseMapping)

def createSample(order, variblesMapping,dependencices, reverseMapping, cpts):
    for i in order:
        alpha = reverseMapping[i]
        if dependencies[aplha] == 0:
        
        else:
            
    


def rejectionSampling(order, variableMapping, dependices, reverseMapping, cpts):
    noOfSamples = 0
    favCases = 0
    while noOfSamples != 10000:
        sample = createSample(order, variblesMapping, cpts, dependices) #sample is created in the form of alphabets
        if consistent(sample, q):
            noOfSamples += 1
            crt = False
            for requried in q[0]: #checking if favoriable or not
                if len(requried) == 1:
                    aplha = required
                else:
                    aplha = required[1:]
                if sample[order[varibleMapping[alpha]]] = required:
                    crt = True
            if crt == True:
                favCases += 1


if __name__ == "__main__":
    graph = collections.defaultdict(list)
    graph = { 
               'a' : ['b', 'c'],
               'b' : ['c'],
               'c' : ['d'],
               'd' : [],
               'e' : ['d']
            }
    
    a = [0.3, 0.7]
    e = [0.35, 0.65]
    b = collections.defaultdict(list)
    b = {
          'a' : [0.1, 0.9],
          '~a' : [0.6, 0.4]
        }
    c = collections.defaultdict(lambda : defaultdict(list))
    c = {
           'a' :{
                  'b' : [0.05, 0.95],
                  '~b' : [0.5, 0.5]
                },

            '~a':{ 
                   'b' : [0.45, 0.55],
                   '~b' : [0.6, 0.4]
                }
        }
    d = collections.defaultdict(lambda : defaultdict(list))
    d = {
           'c' :{
                  'e' : [0.01, 0.99],
                  '~e' : [0.5, 0.5]
                },

            '~c':{ 
                   'e' : [0.75, 0.25],
                   '~e' : [0.31, 0.69]
                }
        }
    
    order, variableMapping, reverseMapping = preProcessing(graph)
 
    
    dependencies = collections.defualtdict(list)
    dependencies = {
                      'a' : []
                      'b' : ['a']
                      'c' : ['a', 'b']
                      'd' : ['c', 'e']
                      'e' : []
                   }
    
   
    cpt = {
            0 : a 
            1 : b
            2 : c 
            3 : d
            4 : e
          }
  
    query = [['a'], ['~c']]
    ans = rejectionSampling(order, varialeMapping, dependecies, query, cpt)
    
