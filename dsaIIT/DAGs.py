'''
Directed Acyclic Graphs

- Represent constraints as a directed graph
    - Vertices are tasks
    - Edge (t,u) if task t has to be completed before task u

- G=(V,E) , a directed graph without directed cycles

- Find a schedule
    - Enumerate V={0,1,...,n-1}
    such that for any (i,j) belongs to E,i appears before j
    - Topological Sorting
'''

'''
TOPOLOGICAL SORTING
- DAGs 
    - G=(V,E), a directed graph without directed cycles

- Topological sorting
    - Enumerate V={0,1,....,n-1} such that for any (i,j) belongs to E,i apppears before j

- represents a feasible schedule

- A graph with directed cycles cannot be sorted topologically

- Path i->j means i must be listed before j
- Cycle=> vertices i,j such that there are paths i->j and j->i
- i must appear before j, and j must appear before i, impossible!

STRATEGY

- First list vertices with no dependencies

- As we proceed, list vertices whose dependencies have already been listed

- ...

ALGORITHM

- A vertex with no dependencies has no incoming edges, indegree(v)=0
- Start with any vertex with indegree >0
- Follow edge back to one of its predecessors
- Repeat o long as indegree >0
- If we repeat n times, we must have a cycle, which is impossible in a DAG

'''

'''
- List out a vertex j with indegree=0
- Delete j and all edges from j
- What remains is again a DAG
- Can find another vertex with indegree=0 to list and eliminate
- Repeat till all the vertices are listed

- Compute indegree of each vertex
    - scan each column of the adjaceny matrix
- List a vertex with indegree 0 and remove it from the DAG
- Update indegrees
- Can find another vertex with indegree=0 to list and eliminate
- Repeat till all vertices are listed
'''

def toposort(AMat):
    '''
    - Compute indegrees by scanning columns of adjacency matrix
    - List a vertex with indegree 0 and remove it from the DAG
    - Update indegrees
    - Repeat till all vertices are listed
    '''
    (rows,cols)=AMat.shape
    indegree={}
    toposortlist=[]
    for c in range(cols):
        indegree[c]=0
        for r in range(rows):
            if AMat[r,c]==1:
                indegree[c]=indegree[c]+1
    for i in range(rows):
        j=min([k for k in range(cols) if indegree[k]==0])
        toposortlist.append(j)
        indegree[j]=indegree[j]-1
        for k in range(cols):
            if AMat[j,k]==1:
                indegree[k]=indegree[k]-1
    return (toposortlist)
'''
Analysis
- Initializing indegrees is O(n**2)
- Loop to enumerate vertices runs n times
    - Identify next vertex to enumerate: O(n)
    - Updating indegrees: O(n)
- Overall O(n**2)
'''

class Queue:
    def __init__(self):
        self.queue=[]
    def addq(self,v):
        self.queue.append()
    def delq(self):
        v=None
        if not self.queue.isempty():
            v=self.queue[0]
            self.queue[1:]
        return v
    def isempty(self):
        return (self.queue==[])
    def __str__(self):
        return (str(self.queue))
            
def topoSortList(AList):
    '''
    - Compute indegrees by scanning adjacency lists
    - maintain queue of vertices with indegree 0
    - Enumerate head of queue, update indegrees add indegree 0 to queue
    - Repeat till queue is empty
    '''
    (indegree,toposortlist)=({},[])
    for u in AList.keys():
        indegree[u]=0
    for u in AList.keys():
        for v in AList[u]:
            indegree[v]=indegree[v]+1
    zerodegreeq=Queue()
    for u in AList.keys():
        if indegree[u]==0:
            zerodegreeq.addq(u)
    while(not zerodegreeq.isempty()):
        j=zerodegreeq.delq()
        toposortlist.append(j)
        indegree[j]=indegree[j]-1
        for k in AList[j]:
            indegree[k]=indegree[k]-1
            if indegree[k]==0:
                zerodegreeq.addq(k)
    return (topoSortList)
# Analysis
'''
- initialising indegrees is O(m+n)
- Loop to enumerate vertices runs n times
    - updating indegrees: amortised O(m)
- Overall, O(m+n)
    Choice of which vertex with indegree 0 to list next
'''