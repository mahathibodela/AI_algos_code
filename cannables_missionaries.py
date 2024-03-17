class Node:
    def __init__(self,ld,lh,rd,rh,side,parent):
        self.ld=ld
        self.lh=lh
        self.rd=rd
        self.rh=rh
        self.side=side
        self.parent=parent

def expansion(node):
    #dev,human
    direct=[[1,0],[0,1],[1,1],[2,0],[0,2]]
    children=[]
    pld=node.ld
    plh=node.lh
    prd=node.rd
    prh=node.rh
    
    for dd,dh in direct:
        if not node.side:
            nld=pld-dd
            nlh=plh-dh
            nrd=prd+dd
            nrh=prh+dh
        else:
            nld=pld+dd
            nlh=plh+dh
            nrd=prd-dd
            nrh=prh-dh
        if min(nld,nlh,nrd,nrh)>=0 and max(nld,nlh,nrd,nrh)<=3 and ((nlh==0) or(nld<=nlh)) and ((nrh==0) or (nrd<=nrh)):
            children.append(Node(nld,nlh,nrd,nrh,not node.side,node))

    return children


def isGoal(node):
    if node.rd==3 and node.rh==3 and node.side:
        return True
    return False

def bfs(intial):
    q=[]
    vis=set()
    q.append(intial)
    vis.add((intial.ld,intial.lh,intial.rd,intial.rh,intial.side))
    found=0

    while q:
        node=q.pop(0)
        
        if isGoal(node):
            found=1
            break
        
        for adjNode in expansion(node):
            if (adjNode.ld,adjNode.lh,adjNode.rd,adjNode.rh,adjNode.side) not in vis:
                vis.add(adjNode)
                q.append(adjNode)
    
    if found==1:
        ans=[]
        while node!=None:
            ans.append(node)
            node=node.parent
        ans.reverse()
        for path in ans:
            print(path.ld,path.lh,"|",path.rd,path.rh,"|")
    else:
        print("solution not found")
    
if __name__ == "__main__":
    bfs(Node(3,3,0,0,False,None))
    


        
