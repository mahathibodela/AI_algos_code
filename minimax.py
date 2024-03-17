def isTerminal(matrix):
    flag = True
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == '-':
                flag = False
                break
    if flag == True: 
        return 0
    
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2]:
            if matrix[i][0] == 'X':
                return 1
            elif matrix[i][0] == 'O':
                return -1
    
    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i]:
            if matrix[0][i] == 'X':
                return 1
            elif matrix[0][i] == 'O':
                return -1
    
    return 100
    


def expansion(matrix, k):
    children = []
    if k == 1:
        for i in range(3):
            for j in range(3):
                if matrix[i][j] == '-':
                    matrix[i][j] = 'X'
                    children.append(matrix)
                    matrix[i][j] = '-'
    else:
        for i in range(3):
            for j in range(3):
                if matrix[i][j] == '-':
                    matrix[i][j] = 'X'
                    children.append(matrix)
                    matrix[i][j] = '-'

    return children

                
def maximise(matrix):
    print("max")
    k = isTerminal(matrix)
    if -1 <= k <= 1:
        return k 
    
    children = expansion(matrix, 1)
    ans = -(10**3)
    for child in children:
        print(child)
        k = minimise(child)
        if k > ans:
            ans = k 
    return ans 

def minimise(matrix):
    k = isTerminal(matrix)
    if -1 <= k <= 1:
        return k 
    
    children = expansion(matrix, 0)
    ans = (10**3)
    for child in children:
        print(child)
        k = maximise(child)
        if k < ans:
            ans = k 
    return ans 
    

def choice(matrix):
    maxMatrix = []
    ans = -(10**3)

    children = expansion(matrix, 1)
    for child in children:
        print(child)
        k = maximise(child)
        if k > ans:
            ans = k 
            maxMatrix = child
    
    return maxMatrix


if __name__ == "__main__":
    matrix = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    print(matrix)

    while True:
        print("computer's move ")
        matrix = choice(matrix)
        print(matrix)
        print("enter your move ")
        i, j = map(int, input().split())
        matrix[i][j] = "O"
        print(matrix)
