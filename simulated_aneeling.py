import math
import random

def isAttack(pos1,pos2):
    r1,c1=pos1
    r2,c2=pos2

    if r1==r2 or c1==c2:
        return True
        
    if abs(r1-r2)==abs(c1-c2):
        return True

    return False

def computing(pos):
    #input is in the format of [[r,c]...]
    
    tot=0
    for i in range(len(pos)):
        for j in range(i+1,len(pos)):
            if isAttack(pos[i],pos[j]):
                tot+=1
    return 28-tot

def compute(state):
    #here the objValue is 1/no of queens attacking each other
    queen_pos=[]
    for i in range(len(state)):
        queen_pos.append((i,int(state[i])-1))
    value=computing(queen_pos)
    return value


def expansion(state):
    children=[]
    for i in range(len(state)):
        k=random.randrange(7)+1
        temp=state[:k]+str(k)+state[k+1:]
        children.append(temp)
    return children


def simulated_anneling(intial,value,best,bestObj,T):
    print(intial)
    if math.floor(T)==0:
        return best,bestObj
    children=expansion(intial)
    selected=random.choice(children)
    children_value=compute(selected)
    if children_value>value:
        return simulated_anneling(selected,children_value,children,children_value,T*0.9)
    
    delta_e=value-children_value
    req_prop=math.exp(delta_e/T)
    prop=random.random()
    if req_prop<=prop:
        return simulated_anneling(selected,children_value,best,bestObj,T*0.9)
    return simulated_anneling(intial,children_value,children,children_value,T*0.9)
    

if __name__ == "__main__":
    intial_states="24748552"
    best=""
    k=compute(intial_states)
    best,bestObj=simulated_anneling(intial_states,k,intial_states,k,100)
    print(best,bestObj)