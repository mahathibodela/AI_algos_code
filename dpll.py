def findPure(qs, symbols):
    for literal in symbols:
        pos, neg = 0, 0
        for clause in qs:
            if literal in clause:
                pos += 1
            if '~'+literal in clause:
                neg += 1
            if pos > 0 and neg > 0:
                break
        if pos > 0 and neg == 0:
            return (literal, True)
        if neg > 0 and pos == 0:
            return (literal, False)

    return ('-', False)


def findUnit(qs):
    for clause in qs:
        if len(clause) == 1:
            for i in clause: #cheking ki wo normal hain ya nehi 
                if len(i) == 1:
                    return (i, True)
                else:
                    return (i[1:], False)
    return ('-', False)

def change(symbol, value, qs, valu):
    # symbol yaha without NEGATION hi ayega
    # symbol value - True -- remove the clause
    # symobl value - False -- remove the literal from the clause
    # ~ || normal -- check karna
    print(symbol, value)
    nqs = []
    nsymbols = set()
    neg = '~'+symbol 
    for clause in qs:
        temp = clause
        if (value == True and symbol in clause) or (value == False and  neg in clause):
            continue
        for literal in temp:
            if literal == symbol or literal == neg:
                temp.remove(literal)
            if len(literal) == 2:
                nsymbols.add(literal[1:])
            else:
                nsymbols.add(literal)
        nqs.append(temp)

    return (nqs, nsymbols)
  
def dpllSerious(qs, symbols, assignments):
    print(qs)
    print(symbols)
    print(assignments)
    print("--------------------------------------------------")
    #depicts all are true
    if len(qs) == 0:
        return True
    
    #find pure symbol
    literal, value = findPure(qs, symbols)
    if literal != '-':
        assignments[literal] = value
        nqs, nsymbols = change(literal, value, qs, value)
        if dpllSerious(nqs, nsymbols, assignments) == True:
            return True
        assignments.remove(literal)

    #find unit symbol
    literal, value = findUnit(qs)
    if literal != '-':
        assignments[literal] = value
        nqs, nsymbols = change(literal, value, qs, value)
        if dpllSerious(nqs, nsymbols, assignments) == True:
            return True
        assignments.remove(literal)
    
    #trying True for the literal first
    for i in symbols:
        literal = i
        break

    assignments[literal] = True
    nqs, nsymbols = change(literal, value, qs, value)
    if dpllSerious(nqs, nsymbols, assignments) == True:
        return True
    
    assigments[literal] = False
    nqs, nsymbols = change(literal, value, qs, value)
    if dpllSerious(nqs, nsymbols, assignments) == True:
        return True
    return False

        

def dpll(intial):
    literals = set()
    qs = []
    assignments = {}
    
    #constuction of modified qs & symbols
    #every clause is represented as  list of sets -- qs
    #all symbols -- literal
    for clause in intial:
        temp = set()
        for literal in clause:
            if len(literal) == 2:
                literals.add(literal[1:])
            else:
                literals.add(literal)
            temp.add(literal)
        qs.append(temp)

    print(qs)
    print(literals)
    k = dpllSerious(qs, literals, assignments)
    return (k, assignments)
    

if __name__ == "__main__":
   qs = [['a', 'b', 'c'], ['a', '~b'], ['a', '~c'], ['~a', 'c']]
   qs = [['~p', 'q'], ['~q', 'r'], ['~r']]
   target = 'c'
   k, assignments = dpll(qs)
   if k == True:
    print(assignments)
   else:
    print("this is invalid")