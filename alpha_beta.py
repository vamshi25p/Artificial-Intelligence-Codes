# Python3 program to demonstrate 
# working of Alpha-Beta Pruning 

# Initial values of Alpha and Beta 
MAX, MIN = 1000, -1000

# Returns optimal value for current player 
# (Initially called for root and maximizer) 
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta, pruned_nodes): 
    # Terminating condition. i.e., leaf node is reached 
    if depth == 3: 
        print(f"Depth: {depth}, Node Index: {nodeIndex}, Value: {values[nodeIndex]}")
        return values[nodeIndex] 

    if maximizingPlayer: 
        best = MIN

        # Recur for each child node 
        for i in range(0, 3): 
            print(f"Depth: {depth}, Node Index: {nodeIndex}, Alpha: {alpha}, Beta: {beta}")
            val = minimax(depth + 1, nodeIndex * 3 + i, False, values, alpha, beta, pruned_nodes) 
            best = max(best, val) 
            alpha = max(alpha, best) 

            # Alpha Beta Pruning 
            if beta <= alpha: 
                print(f"Pruned at Depth: {depth}, Node Index: {nodeIndex * 3 + i}, Alpha: {alpha}, Beta: {beta}")
                pruned_nodes.append((depth + 1, nodeIndex * 3 + i))
                break
        
        return best 
    
    else:
        best = MAX

        # Recur for each child node 
        for i in range(0, 3): 
            print(f"Depth: {depth}, Node Index: {nodeIndex}, Alpha: {alpha}, Beta: {beta}")
            val = minimax(depth + 1, nodeIndex * 3 + i, True, values, alpha, beta, pruned_nodes) 
            best = min(best, val) 
            beta = min(beta, best) 

            # Alpha Beta Pruning 
            if beta <= alpha: 
                print(f"Pruned at Depth: {depth}, Node Index: {nodeIndex * 3 + i}, Alpha: {alpha}, Beta: {beta}")
                pruned_nodes.append((depth + 1, nodeIndex * 3 + i))
                break
        
        return best 

# Driver Code 
if __name__ == "__main__":  # Corrected main block
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    pruned_nodes = []
    optimal_value = minimax(0, 0, True, values, MIN, MAX, pruned_nodes)
    print("Maximum score for the maximizing player (root node):", optimal_value)
    print("Pruned nodes:", pruned_nodes)
