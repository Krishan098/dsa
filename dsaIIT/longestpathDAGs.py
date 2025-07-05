'''
Longest Path
- Find the longest path in a DAG
- if indegree(i)=0, lngest-path-to(i)=0
- if indegree(i)>0, longest path to i is  1 more than longest path to its incoming neighbours
    - longest-path-to(i)= 1+max{longest-path-to(j)|(j,i) belongs to E}
o> To compute longest-path-to(i) need longest-path-to(k) for each incoming neighbour k
o> If graph is topologically sorted, k is listed before i
o> Hence compute longest-path-to() in topological order
'''

'''
o> Let i_0,i_1,....,i_n01 be a topological ordering of V
- All neighbours of i_k appear before it in this list
- From left to right, compute longest-path-to(i_k) as 1+max{longest-path-to(i_j)|(i_j,i_k)belongs to E}
- Overall this computation with topological sorting.

- Compute indegree of each vertex
    - Scan each column of the adjacency matrix
- Initialise textlongest-path-to to 0 for all vertices
- List a vertex with indegree 0 and remove it from the DAG
- Update indegrees, longest path
- Repeat till all vertices are listed
'''
class Queue:
    def __init__(self):
        self.queue=[]
    def addq(self,v):
        return self.queue.append(v)
    def delq(self):
        v=None
        if not self.queue.isempty():
            v=self.queue[0]
            queue=self.queue[1:]
        return v
    def isempty(self):
        return (self.queue==[])
    def __str__(self):
        return (str(self.queue))
def longestpathlist(Alist):
    '''
    - Compute indegrees by scanning adjacency lists
    - Maintain queue of vertices with indegree 0
    - Process head of queue: update indegrees, update queue, update longest paths
    - Repeat till queue is empty
    '''
    (indegree,lpath)=({},{})
    for u in Alist.keys():
        (indegree[u],lpath[u])=(0,0)
    for u in Alist.keys():
        for v in Alist[u]:
            indegree[v]=indegree[v]+1
    zerodegreeq=Queue()
    for u in Alist.keys():
        if indegree[u]==0:
            zerodegreeq.addq(u)
    while (not zerodegreeq.isempty()):
        j=zerodegreeq.delq()
        indegree[j]=indegree[j]-1
        for k in Alist[j]:
            indegree[k]=indegree[k]-1
            lpath[k]=max(lpath[k],lpath[j]+1)
            if indegree[k]==0:
                zerodegreeq.addq(k)
        return (lpath)    
# Analysis
'''
- initializing indegrees is O(m+n)
- Loop to enumerate vertices runs n times.
    - Updating indegrees, longest path: amortised O(m)
'''