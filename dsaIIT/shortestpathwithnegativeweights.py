# Single source shortest path with negative edge weights
'''
- negative edge weights are allowed but no negative cycles
- Going around a cycle can only add to the length
- Shortest route to every vertex is a path, no loops
'''

'''
- suppose minimum weight path from 0 to k is 
    0(w1)->j1(w2)->j2->(w3)---jl-1(wl)->k
    - need not be minimum in terms of number of edges
- Every prefix of this path must itself be a minimum weight path
- Once we discover shortest path to jl-1, next update will fix the shortest path to k
- Repeatedly update shortest distance to each vertex based on shortest distance to its neighbours
    - Update cannot push this distance below actual shortest distance
- after l updates,all shortest paths using <=l edges have stabilized
    - Minimum weight path to any node has at most n-1 edges
    - after n-1 updates, all shortest paths have stabilized
    
'''

# Bellman-Ford algorithm
'''
Initialization 
- D(j): minimum distance known so far to vertex j
- D(j)= {
    0, if j=0
    inf, otherwise
    }
- repeat n-1 times
    - for each vertex j belongs to {0,1,....,n-1},
    for each edge(j,k) belongs to E,
    D(k)= min(D(k),D(j)+W(j,k))
'''
import numpy as np
def bellmanford(WMat,s):
    (rows,cols,x)=WMat.shape
    infinity=np.max(WMat)*rows+1
    distance={}
    for v in range(rows):
        distance[v]=infinity
    distance[s]=0
    for i in range(rows):
        for u in range(rows):
            for v in range(cols):
                if WMat[u,v,0]==1:
                    distance[v]=min(distance[v],distance[u]+WMat[u,v,1])
    return (distance)
'''
Complexity
O(n**3)
'''

# Adjacency list
def BellmanFordList(WList,s):
    infinity=1+len(WList.keys())*max([d for u in WList.keys() for (v,d) in WList[u]])
    distance={}
    for v in WList.keys():
        distance[v]=infinity
    distance[s]=0
    for i in WList.keys():
        for u in WList.keys():
            for (v,d) in WList[u]:
                distance[v]=min(distance[v],distance[u]+d)
    return(distance)
'''
Complexity
- Overall O(m*n)~O(n**3)
'''