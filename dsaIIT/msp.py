# Min cost spanning tree
'''
- SPANNING TREE
- retain a minimal set of edges so that graph remains connected
- recall that a minimally connected graph is a tree
    - Adding an edge to a tree creates a loop
    - Removing an edge disconnects the graph
- Want a tree that connects all the vertices - spanning tree
- more than one spanning tree, in general 
'''
# Minimum cost spanning tree
'''
- Add the cost of all the edges in the tree
- Among the different spanning trees, choose one with minimum cost
'''

'''
- A tree is a connected acyclic graph
- A tree on n vertices has exactly n-1 edges
- Initially, one single component
- Deleting edge (i,j) must split component
    - Otherwise, there is still a path from i to j, combine with (i,j) to form cycle
- Each edge deletion creates one more component
- Deleting n-1 edges creates n components, each an isolated vertex
'''

'''
- Adding an edge to a tree must create a cycle
- Suppose we add an edge(i,j)
- Tree is connected, so there is already a path from i to j
- The new edge (i,j) combined with this path from i to j forms a cycle
'''
'''
- In a  tree, every pair of vertices is connected by a unique path
- If there are 2 paths from i to j, there must be a cycle
'''

# Prim's algo
'''
- Start with the smallest edge and grow a tree
'''

# Kruskal's algo
'''
Scan the edges in ascending order of weight to connect components without forming cycles
'''