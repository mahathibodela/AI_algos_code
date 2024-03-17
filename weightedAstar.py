import heapq
import random
import time
import psutil
import copy 
import collections
from typing import List,Optional
import heapq

class Node:
    def __init__(self,parent,state,g,h):
        self.parent=parent
        self.state=state
        self.g=g 
        self.h=h
    def __lt__(self, other):
        return self.g +2*self.h< other.g +2*other.h


def findPos(arr,k):
    # print(arr,"here")
    for i in range(3):
        for j in range(3):
            if(arr[i][j]==k):
                return (i,j)
    return (0,0)

def hearsitic(start,goal):
    count=0
    for i in range(3):
        for j in range(3):
            if start[i][j]!=0:
                gr,gc=findPos(goal,start[i][j])
                count+=abs(i-gr)+abs(j-gc)
    return count

def expansion(box):
    blank_r,blank_c=findPos(box,0)
    direct=[[0,1],[-1,0],[0,-1],[1,0]]

    child=[]
    for dr,dc in direct:
        r=dr+blank_r
        c=dc+blank_c
        if(0<=r and r<3 and 0<=c and c<3):
            temp=copy.deepcopy(box)
            temp[blank_r][blank_c]=temp[r][c]
            temp[r][c]=0
            child.append(temp)
    return child


def astar(intial,goal):
    heap=[]
    vis=set()
    found=0

    heapq.heappush(heap,(intial))

    while heap:
        node=heapq.heappop(heap)
        if(goal==node.state):
            found=1
            break
        vis.add(((row) for row in intial.state))

        for neighbour in expansion(node.state):
            neigh_tupple=((row) for row in intial.state)
            if neigh_tupple not in vis:
                g_new=node.g+1
                h_new=hearsitic(neighbour,goal)
                if(node.h - h_new>1):
                    print("hearisitic not good exitttttt")
                new_state=Node(node,neighbour,g_new,h_new)
                heapq.heappush(heap,(new_state))
    
    if found==0:
        print(" no solution")
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


if __name__ == "__main__":
    numbers = list(range(9))
    random.shuffle(numbers)
    qs = [numbers[i:i+3] for i in range(0, 9, 3)]
    qs = [
        [1, 8, 2],
        [0, 4, 3],
        [7, 6, 5]
    ]
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    if(check(qs)==True):
        print("is it not solvacle")
    else:
        astar(Node(None,qs,0,hearsitic(qs,goal)),goal)