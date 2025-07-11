# # Prim's algorithm
# '''
# - Incremently grow the minimum cost spanning tree
# - Start with a smallest weight edge overall
# - Extend the current tree by adding the smallest edge from the tree to a vertex not yet in the tree
# '''
# '''
# G=(V,E), W:E->R
# - Incrementally build an MCST
#     - TV c V : tree vertices, already added to MCST
#     - TE c E : tree edges, already added to MCST
# - Initially, TV=TE=0
# - Choose minimum weight edge e =(i,j)
#     Set TV={i,j}, TE={e} MCST
# - Repeat n-2 times
#     - Choose minimum weight edge f=(u,v) such that u belongs to TV, v belongs to TV
#     - Add v to TV, f to TE
# '''
# # Minimum Separator Lemma
# '''
# - Let V be patitioned into tow non-empty sets U and W=V\U
# - Let e=(u,w) be the min cost edge with u belongs to U, w belongs to W.
# - Every MCST must include e

# - Assume for now, all edge weights distinct
# - Let T be an MCST, E doesnot belong to T
# - T contains a path p from u to w
#     - p starts in U, ends in W
#     - Let f=(u',w') be the first edge on p crossing from U to W
#     - Drop f, add e to get a cheaper spanning tree
# '''
# '''
# - what if 2 edges have the same weight
# - Assign each edge a unique index from 0 to m-1
# - In Prim's algo, TV and W=v\TV partition V
# - Algo picks smallest edge connecting TV and W, which must belong to wvery MCST
# - In fact, for any v belongs to V, {v} and V\{v} form a partition
# - The smallest weight edge leaving any vertex must belong to evry MCST
# - We started with overall minimum cost edge
# - Instead, can start at any vertex v, with TV={v} and TE= 0
# '''

import numpy as np
def primlist(WList):
    '''
    - keep track of 
        - visited[v]- is v in the spanning tree
        - distance[v]- shortest distance from v to the tree
        - TreeEdges- edges in the current spanning tree
    - Initialize visited[v] to False, distance[v] to infinity
    - First add vertex 0 to tree
    - Find edge (u,v) leaving the tree where distance[v] is minimum, add it to the tree, update distance[w] of neighbours
    '''
    infinity=1+max([d for u in WList.keys() for (v,d) in WList[u]])
    (visited,distance,TreeEdges)=({},{},[])
    for v in WList.keys():
        (visited[v],distance[v])=(False,infinity)
    visited[0]=True
    for (v,d) in WList[0]:
        distance[v]=d
    for i in WList.keys():
        (mindist,nextv)=(infinity,None)
        for u in WList.keys():
            for (v,d) in WList[u]:
                if visited[u] and (not visited[v]) and d<mindist:
                    (mindist,nextv,nexte)=(d,v,(u,v))
        if nextv is None:
            break
        visited[nextv]=True
        TreeEdges.append(nexte)
        for (v,d) in WList[nextv]:
            if not visited[v]:
                distance[v]=min(distance[v],d)
    return (TreeEdges)

'''
Complexity
- Initialization -O(n)
- Loop to add nodes to the tree -O(n)
- Each iteration takes O(m) time to find a node to add
- Overall time is O(mn) which could be O(n**3)
'''

def primListoptimized(WList):
    '''
    -visited[v] - is v in the spanning tree
    - distance[v] - shortest distance from v to the tree
    - nbr[v] - nearest neighbour oof v in tree
    - scan all non-tree vertices to find nextv with min distance
    - Then (nbr[nextv],nextv) is the tree edge to add
    - Update distance[v] and nbr[v] for all neighbours of nextv
    '''
    infinity=1+max([d for u in WList.keys() for (v,d) in WList[u]])
    (visited,distance,nbr)=({},{},{})
    for v in WList.keys():
        (visited[v],distance[v],nbr[v])=(False,infinity,-1)
    visited[0]=True
    for (v,d) in WList[0]:
        (distance[v],nbr[v])=(d,0)
    for i in range(1,len(WList.keys())):
        nextd=min([distance[v] for v in WList.keys() if not visited[v]])
        nextvlist=[v for v in WList.keys() if (not visited[v]) and distance[v]==nextd]
        if nextvlist==[]:
            break
        nextv=min(nextvlist)
        visited[nextv]=True
        # for (v,d) in WList[nextv]:
        #     if not visited[v]:
        #         (distance[v],nbr[v])=(min(distance[v],d),nextv)
        for (v,d) in WList[nextv]:
            if not visited[v]:
                if d < distance[v]:
                    distance[v] = d
                    nbr[v] = nextv
    return (nbr)
'''
Complexity to find the next vertex to add is O(n)
'''

if __name__=='__main__':
    WList = {
        0: [(1, 6), (2, 8),(3,80),],
        1: [(0, 6), (2, 10)],
        2: [(0, 8), (1, 10),(4,20)],
        3: [(0,80),(4,69)],
        4: [(2,20),(3,69)]
    }
    print(primlist(WList))
    print(primListoptimized(WList))    
