

INITIAL_STATE = [
    [1, 4, 2],
    [5, 3, 0]
]

GOAL_STATE = [
    [0, 1, 2],
    [5, 4, 3]
]
class Node:
    def __init__(self, state, parent=None, tile=None):
        self.state = state
        self.parent = parent
        self.tile = tile
    


#function to check for possible tile moves 
def valid_moves(node):
   
    #locate empty tile
    for i, j in enumerate(node.state):
        if 0 in j:
            break
            x = i                  
            y = j                  
    

def find_blank(node):
    blank_coords = []
    for i in range(len(node.state)):
        if 0 in node.state[i]:
            return (i, node.state[i].index(0))
    
    return None

def possible_moves(node):

    #locate empty tile
    v, h = find_blank(node)
    
    #figure out what tiles can move there 
    moves_list = [] 

    #right tile can move 
    if h <= 1:
        moves_list.append([node.state[v][h+1], [v, h+1]])
    
    #left tile can move 
    if h >=1:
        moves_list.append([node.state[v][h-1], [v, h-1]])
    

    #bottom tile can move 
    if v == 0:
        moves_list.append([node.state[v+1][h], [v+1, h]])

    #top tile can move
    if v == 1:
        moves_list.append([node.state[v-1][h], [v-1, h]])

    #return list of those tiles 
    return moves_list 

#find actual tiles that can move specified in moves_list and sort in ascending order 
def sort_moves(moves_list):
   return sorted(moves_list, key = lambda x:x[0], reverse = True)
   
#function to check goal state 
def check_goal(curr, goal):
        return curr[0] == goal[0] and curr[1] == goal[1]


def goal_path(curr):

    path = [] 
    
    while curr:
        path.append(curr.state)
        curr = curr.parent
    

    num_states = 0 
    #now reverse order
    for state in reversed(path):
        num_states += 1 
        print(state)
    print(num_states)


def bfs(root):

    queue = []
    queue.append(root)

    closed_list = set()

    goal_tuple = tuple(map(tuple, GOAL_STATE))

    while queue:
        curr = queue.pop(0)

        curr_tuple = tuple(map(tuple, curr.state))

        #make sure nodes that have already been expanded are not being expanded again
        if curr_tuple in closed_list:
            continue 
        
        #check goal state 
        if goal_tuple == curr_tuple:
            #print out goal path
            print("here")
            goal_path(curr)
            return 
            
        
        #generate possible moves based of current state
        moves = possible_moves(curr)
    
        
        #sort moves based on min tile number 
        sorted_moves = sort_moves(moves)
        
        #add sorted moves to q based on lowest tile 
        for tile in range(len(sorted_moves)):
           
            #make a deep copy of the current state 
            new_state = [row[:] for row in curr.state]
            blank_v, blank_h = find_blank(curr)
            move_v = sorted_moves[tile][1][0]
            move_h = sorted_moves[tile][1][1]


            #swap tiles 
            new_state[blank_v][blank_h], new_state[move_v][move_h] = new_state[move_v][move_h], new_state[blank_v][blank_h]
 

            #create a new node for the new state
            new = Node(new_state, parent = curr, tile = new_state[move_v][move_h])
      
            queue.append(new)
        

        #add curr to closed list 
        closed_list.add(curr_tuple )

    
def dfs(node): 
   
    stack = [node]

    closed_list = set()
    goal_tuple = tuple(map(tuple, GOAL_STATE))

    while stack: 
        curr = stack.pop() 

        curr_tuple = tuple(map(tuple, curr.state))

        #check if node is in closed list:
        if curr_tuple in closed_list:
            continue 

        #check if node is goal state 

        if curr_tuple == goal_tuple:
            goal_path(curr)
            return 
        
        closed_list.add(curr_tuple)

      
        #generate and sort possible moves 
        moves = possible_moves(curr)
        sorted_moves = sort_moves(moves)
        
       
        for tile in range(len(sorted_moves)):
            
            print("current tile: ", sorted_moves[tile] )
            
            #make a deep copy of the current state 
            new_state = [row[:] for row in curr.state]
            blank_v, blank_h = find_blank(curr)
            move_v = sorted_moves[tile][1][0]
            move_h = sorted_moves[tile][1][1]

            #swap tiles 
            new_state[blank_v][blank_h], new_state[move_v][move_h] = new_state[move_v][move_h], new_state[blank_v][blank_h]

            #create a new node for the new state
            new = Node(new_state, parent = curr, tile = new_state[move_v][move_h])

            stack.append(new)



def main():
    root = Node(INITIAL_STATE)
    dfs(root)


if __name__ == "__main__":
    main()






        


