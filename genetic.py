import math
import bisect
import random

def isAttack(pos1,pos2):
    r1,c1=pos1
    r2,c2=pos2

    if r1==r2 or c1==c2:
        return True
        
    if abs(r1-r2)==abs(c1-c2):
        return True

    return False

def compute(pos):
    #input is in the format of [[r,c]...]
    
    tot=0
    for i in range(len(pos)):
        for j in range(i+1,len(pos)):
            if isAttack(pos[i],pos[j]):
                tot+=1
    return 28-tot

def computeObjective(states,best,bestObj):
    #here the objValue is 1/no of queens attacking each other
    objective_value=[]

    for j,state in enumerate(states):
        queen_pos=[]
        for i in range(len(state)):
            queen_pos.append((i,int(state[i])-1))
        value=compute(queen_pos)
        if value>bestObj:
            best=state
            bestObj=value
        objective_value.append(value)
        
    return objective_value,best,bestObj

def geneticAlgo(states,n,best,bestObj,time):
    if time==0:
        return (best,bestObj) # --- YE NICHE HONA HAIN..
    print(states)
    #objective value agaya
    objective_value,best,bestObj=computeObjective(states,best,bestObj)
    
    #percentage finding
    summ=0
    for i in objective_value:
        summ+=i
    propability=[int(math.floor((i/summ)*100)) for i in objective_value]
    percentage_prop=[]
    tot=0
    for i in propability:
        tot+=i 
        percentage_prop.append(tot)

    parent_map={value:i for i,value in enumerate(percentage_prop)}
    max_value=percentage_prop[-1]
    
    
    #picking parent based on the probability
    children=[]
    for i in range(2):
        random_parent=[]
        sub_children=[]
        for j in range(2):
            random_no=random.randrange(max_value)
            a=bisect.bisect_left(percentage_prop,random_no)
            random_parent.append(states[a])

        #finding the crossover point randomly
        point=random.randrange(7)+1
        sub_children.append(random_parent[0][:point+1]+random_parent[1][point+1:])
        sub_children.append(random_parent[1][:point+1]+random_parent[0][point+1:])

        #making mutations randomly,will mutate with a probability 60
        for j in range(2):
            prob=random.randrange(100)
            if prob<=60:
                mutate_point=random.randrange(7)+1
                mutate_replace=random.randrange(7)+1
                sub_children[j]=sub_children[j][:mutate_point]+str(mutate_replace)+sub_children[j][mutate_point+1:]
        
        for j in sub_children:
            children.append(j)
            # print(j)
    
    #calling the function again
    return geneticAlgo(children,n,best,bestObj,time-1)


if __name__ == "__main__":
    intial_states=["24748552","32752411","24415124","32543213"]
    best=""
    best,bestObj=geneticAlgo(intial_states,4,best,-float(1e9),100)
    print(best,bestObj)
    