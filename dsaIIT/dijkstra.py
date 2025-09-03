# Single source shortest paths
'''
- Weighted graph:
    - G=(V,E)
    - W: E->R
- Single source shortest paths
    - Find shortest paths from a fixed vertex to every other vertex
- Assume, for now that edge weights are all non-negative
- Compute shortest paths from 0 to all vertices
- Imagine vertices are oil depots, edges are pipelines
- set fire to oil depot at the vertex 0
- Fire travels at a uniform speed along each pipeline
- First oil depot to catch fire after 0 is nearest vertex
- Next oil depot is second nearest vertex
- compute expected burn time for each vertex
- Each time a new vertex burns, update the expected burn times of its neighbours
'''

# Dijkstra's algorithm
# Greedy 
'''
- Each new shortest path we discover extends an earlier one
- By induction, assume we have found shortest paths to all vertices already burnt
- Next vertex to burn is v, via x
- Cannot find a shorter path later from y to v via w
    - Burn time of w>= burn time of v
    - Edge from w to v has weight >=0
- This argument breaks down if edge(w,v) can have negative weight
    - Can't use Dijkstra's algorithm with negative edge weights.
'''

# Implementation
'''
- Maintain two dictionaries with vertices as keys
    - visited, initally False for all v 
    - distance, initally infinity for all v
- Set distance[s] to 0
- Repeat, until all reachable vertices are visited
    - Find unvisited vertex nextv with minimum distance
    - Set visited[nextv] to True
    - Recompute distance[v] for every neighbour v of nextv
'''
import numpy as np
def dijkstra(WMat,s):# s-> source matrix; WMat-> weighted adjacency matric
    (rows,cols,x)=WMat.shape# 2 dimensional matrix ; x-> x=0,edge;x=1,weight
    infinity=np.max(WMat)*rows+1
    (visited,distance)=({},{})
    for v in range(rows):
        (visited[v],distance[v])=(False,infinity)
    distance[s]=0
    for u in range(rows):
        nextd=min([distance[v] for v in range(rows) if not visited[v]])
        nextvlist=[v for v in range(rows) if (not visited[v]) and distance[v]==nextd]
        if nextvlist==[]:
            break
        nextv=min(nextvlist)
        visited[nextv]=True
        for v in range(cols):
            if WMat[nextv,v,0]==1 and (not visited[v]):
                distance[v]=min(distance[v],distance[nextv]+WMat[nextv,v,1])
    return (distance)
# Complexity
'''
- Setting infinity takes O(n**2) time
- Main loop runs n times
    - Each iteration visits one more vertex
    - O(n) to find next vertex to visit
    - O(n) to update distance[v] for neighbours
- Overall O(n**2)
'''

def dijkstralist(WList,s):
    infinity=1+ len(WList.keys())*max([d for u in WList.keys() for (v,d ) in WList[u]])
    (visited,distance)=({},{})
    for v in WList.keys():
        (visited[v],distance[v])=(False,infinity)
    distance[s]=0
    for u in WList.keys():
        nextd=min([distance[v] for v in WList.keys() if not visited[v]])
        nextvlist=[v for v in WList.keys() if (not visited[v]) and distance[v]==nextd]    
        if nextvlist==[]:
            break
        nextv=min(nextvlist)
        visited[nextv]=True
        for (v,d) in WList[nextv]:
            if not visited[v]:
                distance[v]=min(distance[v],distance[nextv])
    return (distance)
#Complexity
'''
- setting infinty and updating distances both O(m), amortised
- Overall O(n**2) 
'''