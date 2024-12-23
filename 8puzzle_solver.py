from simpleai.search import astar, SearchProblem


class PuzzleSolver(SearchProblem):
    def actions(self, cur_state):
        rows = string_to_list(cur_state)
        row_empty, col_empty = get_location(rows, 'e')
        actions = []
        if row_empty > 0:
            actions.append(rows[row_empty-1][col_empty])
        if row_empty < 2:
            actions.append(rows[row_empty+1][col_empty])
        if col_empty > 0:
            actions.append(rows[row_empty][col_empty-1])
        if col_empty < 2:
            actions.append(rows[row_empty][col_empty+1])
        return actions 
    def result(self,state,action): 
        rows=string_to_list(state)
        row_empty,col_empty=get_location(rows,'e')
        row_new,col_new=get_location(rows,action)
        rows[row_empty][col_empty],rows[row_new][col_new]=rows[row_new][col_new],rows[row_empty][col_empty]
        return list_to_string(rows) 
    def is_goal(self,state): 
        return state==GOAL
    def heuristic(self,state): 
        rows=string_to_list(state) 
        distance=0 
        for n in '12345678e': 
            row_new,col_new=get_location(rows,n) 
            row_new_goal,col_new_goal=goal_positions[n] 
            distance+=abs(row_new-row_new_goal)+abs(col_new-col_new_goal) 
        return distance 
def list_to_string(input_list): 
    return '\n'.join(['-'.join(x) for x in input_list]) 
def string_to_list(input_string): 
    return [x.split('-') for x in input_string.split('\n')] 
def get_location(rows,input_element): 
    for i,row in enumerate(rows): 
        for j,item in enumerate(row): 
            if item==input_element: 
                return i,j  
GOAL='''1-2-3
4-5-6
7-8-e''' 
INITIAL='''1-e-2
6-3-4
7-5-8'''
goal_positions={} 
rows_goal=string_to_list(GOAL) 
for n in '12345678e': 
    goal_positions[n]=get_location(rows_goal,n) 
result=astar(PuzzleSolver(INITIAL)) 
for i,(action,state) in enumerate(result.path()): 
    print() 
    if action==None: 
        print('Initial Configuration') 
    elif i==len(result.path())-1: 
        print('After moving',action,'into the empty space.Goal Acheived!') 
    else: 
        print('After moving',action,'into the empty space') 
    print(state) 

        
            