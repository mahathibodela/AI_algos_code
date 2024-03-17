import collections
def forwardChaining(qs, target):
    infered = {} #
    countForDummi = [] #ek dumy variable set hone keliye kitna literals chahiye
    inPremise = collections.defaultdict(list) #ek ek syllable kis kis syllable ka left side main hain
    dummiMap = [] #dummi variable for each right side syllable
    q = []
    n = len(qs)
    
    for i in range(n):
        clause = qs[i]
        left = clause[0]
        right = clause[1]
        infered[right] = False
        if len(left) != 0:
            dummiMap.append(right)
            countForDummi.append(len(left))
            for literal in left:
                inPremise[literal].append(i)
                infered[literal] = False
        else:
            q.append(right)

    while q:
        literal = q.pop(0)
        if infered[literal] == False:
            if literal == target:
                return True
            infered[literal] = True
            for dummi in inPremise[literal]:
                countForDummi[dummi] = countForDummi[dummi] - 1
                if countForDummi[dummi] == 0:
                    q.append(dummiMap[dummi])
    
    return False


if __name__ == "__main__":
    qs = [[['p'],'q'],[['l', 'm'], 'p'], [['b', 'l'], 'm'], [['a', 'p'],'l'], [['a', 'b'], 'l'], [[],'a'], [[], 'b']]
    target = 'q'
    k = forwardChaining(qs, target)
    print(k)