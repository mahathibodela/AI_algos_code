class Search:
    def check(self,st:State) -> bool:
        inv_count = 0
        mat = st.state
        arr = list()
        for i in mat:
            arr.extend(i)
        empty_value = 0
        for i in range(0, 9):
            for j in range(i + 1, 9):
                if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                    inv_count += 1
                else:
                    continue

        if inv_count%2 != 0:
            return False
        else:
            return True

    def expansion(self,st:State)->List[State]:
        # the actions to be performed
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        blank_row=-1
        blank_column=-1
        result = list()
        for i in range(3):
            for j in range(3):
                if st.state[i][j]==0:
                    blank_row,blank_column=i,j
                    break

        for i in range(4):
            new_state = deepcopy(st.state)
            new_row=blank_row+dr[i]
            new_column=blank_column+dc[i]
            if 0<=new_row<3 and 0<=new_column<3:
                new_state[new_row][new_column],new_state[blank_row][blank_column] = new_state[blank_row][blank_column],new_state[new_row][new_column]
                result.append(State(new_state,st.depth+1,st))
        return result
    def printPath(self,st:State)->List[List[List[int]]]:
        res = list()
        print(type(st))
        while st is not None:
            res.append(st.state)
            st = st.parent
        return res
    def bfs_search(self,start:State,goal:State)->List[List[List[int]]]:
        q = list()
        visited = defaultdict(bool)
        q.append(start)
        visited[start] = True
        rec_count=0
        while q:
            rec_count+=1
            st = q.pop(0)
            if self.check(st) is False:
                return [[[]]]
            if st.state == goal.state:
                return self.printPath(st)
            neighbours = self.expansion(st)
            for i in neighbours:
                if i not in visited:
                    visited[i] = True
                    q.append(i)

        return [[[]]]
    def dfs_search(self, start: State,goal:State) -> List[List[int]]:
        stack = [start]
        visited = set()

        while stack:
            current = stack.pop()

            if current.state == goal.state:
                # Trace back the path and return it
                return self.printPath

            visited.add(current)

            for neighbor in self.expansion(current):
                if self.check(neighbor) is False:
                    return [[]]
                if neighbor not in visited:
                    stack.append(neighbor)

        return [[]]  # No solution found
if __name__ == "__main__":
    state = [[1,8,2],[0,4,3],[7,6,5]]
    state2 = [[1,2,3],[4,5,6],[7,8,0]]
    # for i in range(3): print(*state[i])
    # for i in range(3): print(*state2[i])

    start = State(state,0,None)
    goal = State(state2,0,None)

    s = Search()

    res = s.bfs_search(start,goal)
    if res==[[[]]]:
        print("goal cannot be reached")
    else:
        for i in res:
            for j in i:print(*j)
            print()
    s.dfs_search(start,goal)