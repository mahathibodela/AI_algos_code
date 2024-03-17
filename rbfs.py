import copy
import heapq
class Node:
    def __init__(self,state,parent,g,f):
        self.parent=parent
        self.state=state
        self.g=g 
        self.f=f 

class Search:
    #retruning result[node],cutoff
    def findPos(self,box,k):
        for i in range(3):
            for j in range(3):
                if box[i][j]==k:
                    return (i,j)
        return (0,0)

    def heuristic(self,box,c,goal):
        if c==0:
            count=0
            for i in range(3):
                for j in range(3):
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

    def expansion(self,node,goal):
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
                children.append(Node(temp,node,node.g+1,self.heuristic(temp,c,goal)))
        return children

    def rbfs(self,node,goal,cutoff):
        if node.state==goal:
            return (node,0)
        print(node.state,"this is node ka f ",node.f)
        children=self.expansion(node,goal)

        if len(children)==0:
            return (None,float(1e9))
        
        for adjNode in children:
            adjNode.f=max(node.f,adjNode.f)

        while True:
            sorted(children,key=lambda x:x.f,reverse=True)
            print("these are the children and the following f values")
            for child in children:
                print(child.state,child.f)
            best=alternative=children[0]
            if best.f>cutoff:
                return (None,best.f)
            if len(children)!=1:
                alternative=children[1]
            print(best.f,"-- this is best.f",alternative.f,"--this is the alternative.f")
            result,best.f=self.rbfs(best,goal,min(cutoff,alternative.f))
            
            if result!=None:
                return (result,best.f)
            i+=1

def check(box):
    inversions = 0
    for i in range(len(box)):
        for j in range(i + 1, len(box)):
            if box[i] != 0 and box[i] > box[j]:
                inversions += 1
    return inversions % 2 == 0

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
    somename=Search()
    start=Node(qs,None,0,somename.heuristic(qs,1,goal))
    if(check(qs)!=True):
        print("is it not solvacle")
    else:
        k=somename.rbfs(start,goal,40)
            
            