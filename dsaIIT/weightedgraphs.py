# Shortest path in weigthed graphs
'''
o> Weighted Graphs
    - Recall that BFS explores a graph level by level
    - BFS computes shortest path, in terms of number of edges, to every reachable vertex
    - Many assign values to edges
        - Cost, time, distance
        - Weighted graph
    - G=(V,E), W:E-> R
- Adjacency matrix
    - records weights along with edge information- weight is always 0 if no edge
- Adjacency list
    - Records weights along with edge information
- In a weighted graph, add up the weights along a path
- Weighted shortest path need not have minimum number of edges
'''
# SINGLE SOURCE SHORTEST PATHS
'''
- Find shortest paths from a fixed vertex to every other vertex
- Transport finished product from a factory(single source) to all retail outlets
- Courier company delivers items from distribution centre(single source) to addressees
'''
# ALL PAIRS SHORTEST PATHS
'''
- find shortest paths between every pair of vertices i and j
- Optimal airline, roadway, road routes between cities
'''
# Negative edge weights
'''
- Negative cycles
    - A negative cycle is one whose weight is negative
        - Sum of the weights of edges that make up the cycle
- By repeatedly traversing a negative cycle,total cost keeps decreasing
- If a graph has a negative cycle, shortest paths are not defined
- Without negative cycles, we can compute shortest paths even if some weights are negative
'''