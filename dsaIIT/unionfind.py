# Kruskal's algorithm for MCST
'''
- process edges in ascending order of cost
- if edge (u,v) does not create a cycle, add it
    - (u,v) can be added if u and v are in different components
    - adding edge (u,v) merges these components
- Components partition vertices
    - Collection of disjoint sets
- Need data structure to maintain collection of disjoint sets
    - find(v) - return set containing v
    - union(u,v) - merge sets of u,v
'''
# Union-Find data structure
'''
- A set S partitioned into components {C1,C2,...,Ck}
    - Each s belongs to S to exactly one Cj
- Support the following operations
    - MakeUnionFind(S) - set up initial singleton components {s}, for each s belongs to S
    - Find(s)- return the component containing s
    - Union(s,s')- merges components containing s,s'
'''

# Algo
'''
Assume S={0,1,...,n-1}
Set up a array/dictionary Component
MakeUnionFind(S)- 
    set component[i]=i for each i
Find(i)
    return component[i]
Union(i,j)
    c_old=Component[i]
    c_new=Component[j]
    f
'''