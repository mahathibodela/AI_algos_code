import copy 
import collections
#0--mispalced tiles
#1--manhattan tiles
#2--gasching tiles

class Node:
    def __init__(self,state,parent,g,h):
        self.state=state
        self.parent=parent
        self.g=g 
        self.h=h
class Search:
    def findPos(self,box,k):
        for i in range(3):
            for j in range(3):
                if box[i][j]==k:
                    return (i,j)
        return (0,0)

    def heuristic(self,box,c,goal):
        if c==0:
            count=0
            for i in range(0,3):
                for j in range(0,3):
                    if box[i][j]!=goal[i][j]:
                        count+=1
            return count

        if c==1:
            count=0
            for i in range(3):
                for j in range(3):
                    if box[i][j]!=0:
                        gx,gy=self.findPos(goal,box[i][j])
                        count+=abs(gx-i)+abs(gy-j)
            return count

        if c==2:
            #yaha likna hain abhi
            count=0
            return count

        return 0


    def expansion(self,node,goal,vis):
        box=node.state
        children=[]
        direct=[[0,1],[-1,0],[0,-1],[1,0]]
        blank_x,blank_y=self.findPos(box,0)

        for dr,dc in direct:
            r=dr+blank_x
            c=dc+blank_y
            if(0<=r and r<3 and 0<=0 and c<3):
                temp=copy.deepcopy(box)
                temp[blank_x][blank_y]=temp[r][c]
                temp[r][c]=0
                temp_tupple=(row for rows in temp)
                if temp_tupple not in vis:
                   children.append(Node(temp,node,node.g+1,self.heuristic(temp,c,goal)))
        return children

    def ida(self,node,goal,cutoff,vis,count):
        if node.g+node.h>cutoff:
            return (node.g+node.h,0,None)
        
        if node.state==goal:
            return (0,1,node)
        
        nodeState_tupple=(rows for rows in node.state)
        vis.add(nodeState_tupple)
        minLimit=float(1e9)
        for neighbour in self.expansion(node,goal,vis):
            cost,s,adjNode=self.ida(neighbour,goal,cutoff,vis,count)
            if s==1:
                return (cost,s,adjNode)
            minLimit=min(minLimit,cost)
        
        return (minLimit,0,None)
            

    def idastar(self,intial,goal,limit,count):
        cutoff=intial.g+intial.h
        s=0
        count[0]+=1

        while cutoff<limit and s==0:
            cutoff,s,node=self.ida(intial,goal,cutoff,set(),count)
        
        if s==0:
            print("solution not found")
        else:
            ans=[]
            while node!=None:
                ans.append(node.state)
                node=node.parent
            ans.reverse()

            for path in ans:
                print(path)

def check(box):
    inversions = 0
    for i in range(len(box)):
        for j in range(i + 1, len(box)):
            if box[i] != 0 and box[i] > box[j]:
                inversions += 1
    return inversions % 2 == 0

#ye likna nehi ata wo dekna hain
if __name__ == "__main__":
    numbers = list(range(9))
    # random.shuffle(numbers)
    # qs = (numbers(i:i+3) for i in range(0, 9, 3))
    qs = [
        [5, 3, 0],
        [8, 7, 6],
        [2, 4, 1]
    ]
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    count=[0]
    somename=Search()
    start=Node(qs,None,0,somename.heuristic(qs,0,goal))
    print(count)
    if(check(qs)!=True):
        print("is it not solvacle")
    else:
        somename.idastar(start,goal,100,count)
    print(count[0])

            
        