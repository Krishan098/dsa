# Kruskal's Algorithm
'''
- Start with n components, each a single vertex
- Process edges in ascending order of cost
- Include edge if it doesnot create a cycle
'''

'''
G=(V,E), W:E-> R
- let E= {e0,e1,...,em-1} be edges sorted in ascending order by weight
- Let TE c E be the set of tree edges already added to MCST
- Initially, TE= 0
- Scan E from e0 to em-1
    - If adding ei to TE creates a loop, skip it 
    - Otherwise, add ei to TE
'''
# MINIMUM SEPARATOR LEMMA

def kruskal(WList):
    '''
    Collect edges in a list as(d,u,v)
        - weight as first component for easy sorting
    - main challenge is to keep track of connected components
        - dictionary to record component of each vertex
        - Initially each vertex is an isolated component
        - When we add an edge(u,v), merge the components of u and v
    '''
    (edges,component,TE)=([],{},[])
    for u in WList.keys():
        # Weight as first component to sort easily
        edges.extend([(d,u,v) for (v,d) in WList[u]])
        component[u]=u
    edges.sort()
    print(edges)
    for (d,u,v) in edges:
        if component[u]!=component[v]:
            TE.append((u,v))
            c=component[u]
            for w in WList.keys():
                if component[w]==c:
                    component[w]=component[v]
    return (TE) 
'''
Complexity
    - Sorting is O(mlogm)
        - Since m is at most n**2, equivalently O(mlogn)
- Outer loop runs m times
    - Each time we add a tree edge, we have to merge components - O(n) scan
    - n-1 tree edges so this is done O(n) times
- Overall O(n**2)
''' 



if __name__=='__main__':
    WList= {
    0:[(1,6),(2,8),(3,80)],
    1:[(0,6),(2,10)],
    2:[(0,8),(1,10),(4,20)],
    3:[(0,80),(4,69)],
    4:[(2,20),(3,69)]
}
    print(kruskal(WList))

'''
- Data structure to maintain collection of disjoint sets
    - find(v) - return set containing v
    - union(u,v) - merge sets of u,v

'''

# Efficient union-find brings complexity to O(mlogn)