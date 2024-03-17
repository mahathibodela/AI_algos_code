def resolution(qs):
    clauses2 = []
    clauses1 = []
    clause1Set = set()
    clause2Set = set()
    for clause in qs:
        subClause = ""
        for literal in clause:
            if len(literal) == 1:
                subClause += '*'+str(ord(literal))
            else:
                subClause += '*-'+str(ord(literal[1]))
        subClause += '*'
        clauses2.append(subClause)
        clause2Set.add(subClause)
    
    c = 0
    while True:
        #only with clauses2
        n2 = len(clauses2)
        n1 = len(clauses1)
        newClauseSet = set()
        newClauses = []
        for i in range(n2):
            for j in range(i + 1, n2):
                clause1 = clauses2[i]
                clause2 = clauses2[j]
                pre1 = 0
                for k in range(1,len(clause1)):
                    if clause1[k] == '*':
                        no1S = clause1[pre1 + 1:k]
                        if no1S[0] == '-':
                            no1 = -1 * int(no1S[1:])
                        else:
                            no1 = int(no1S)
                        pre2 = 0
                        for l in range(1,len(clause2)):
                            if clause2[l] == '*':
                                no2S = clause2[pre2 + 1:l]
                                if no2S[0] == '-':
                                    no2 = -1 * int(no2S[1:])
                                else:
                                    no2 = int(no2S)
                                if no1 + no2 == 0:
                                    newClause = clause1[:pre1] + clause1[k:]
                                    sub = clause2[:pre2] + clause2[l:]
                                    newClause += sub[1:]
                                    if len(newClause) == 1:
                                        return True
                                    if newClause not in clause1Set and newClause not in clause2Set:
                                        newClauseSet.add(newClause)
                                        newClauses.append(newClause)
                                pre2 = l
                        pre1 = k
        
        #now for every element in set 2 to for every element in set 1
        for i in range(n2):
            for j in range(n1):
                clause1 = clauses2[i]
                clause2 = clauses1[j]
                pre1 = 0
                for k in range(1,len(clause1)):
                    if clause1[k] == '*':
                        no1S = clause1[pre1 + 1:k]
                        if no1S[0] == '-':
                            no1 = -1 * int(no1S[1:])
                        else:
                            no1 = int(no1S)
                        pre2 = 0
                        for l in range(1,len(clause2)):
                            if clause2[l] == '*':
                                no2S = clause2[pre2 + 1:l]
                                if no2S[0] == '-':
                                    no2 = -1 * int(no2S[1:])
                                else:
                                    no2 = int(no2S)
                                if no1 + no2 == 0:
                                    newClause = clause1[:pre1] + clause1[k:]
                                    sub = clause2[:pre2] + clause2[l:]
                                    newClause += sub[1:]
                                    if len(newClause) == 1:
                                        return True
                                    if newClause not in clause1Set and newClause not in clause2Set:
                                        newClauseSet.add(newClause)
                                        newClauses.append(newClause)
                                pre2 = l
                        pre1 = k


        if len(newClauses) == 0:
            return False
        for clause in clauses2:
            clauses1.append(clause)
        clauses2 = newClauses
        for clause in clause2Set:
            clause1Set.add(clause)
        clause2Set = newClauseSet

if __name__ == "__main__":
    qs = [['~a', 'h'], ['~i', 'h'], ['m', 'a'], ['~m', 'i'], ['~h']]
    k = resolution(qs)
    print(k)
