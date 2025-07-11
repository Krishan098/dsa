# All pairs shortest path
'''
- Find shortest paths between every pair of vertices i and j
- Optimal airline, railway,road routes between cities
'''
# Transitive Closure
'''
- Adjacency matrix A represents paths of length 1
- Matrix multiplication, A**2=AxA
    - A**2[i,j]=1 if there is a path of length 2 from i to j
    - For some k, A[i,k]=A[k,j]=1
- In general, A^(l+1)=A^lxA,
    - A^(l+1)[i,j]=1 if there is a path of length l+1 from i to j
    - For some k, A^l[i,k]=1, A[k,j]=1
- A+=A+A**2+....+A**n-1
'''
# Alternative approach
'''
- B^k[i,j]=1 if there is path from i to j via vertices {0,1,...,k-1}
    - constraint applies only to intermediate vertices between i and j
    - B^0[i,j]=1 if there is a direct edge
    - B^0 =A
- B^(k+1)[i,j]=1 if
    - B^k[i,j]=1 -- can already reach j from i via{0,1,...k-1}
    - B^k[i,k]=1 and B^k[k,j]=1--use {0,1,....k-1} to go from i to k and then from k to j
'''  
# Warshall's algorithm
'''
- B^k[i,j]=1 if there is path from i to j via vertices {0,1,...k-1}
- B^0[i,j]=A[i,j]
    - Direct edges, no intermediate vertices
- B^(k+1)[i,j]=1 if
    - B^k[i,j]=1 or
    - B^k[i,k]=1 and B^k[k,j]=1
- B^n[i,j]=1 if there is some path from i to j with intermediate vertices in {0,1,....,n-1}
- B^n=A+
'''
# Floyd-Warshall algorithm
'''
- Let SP^k[i,j] be the length of the shortest path from i to j via vertices {0,1,...k-1}
- SP^0[i,j]=W[i,j]
    - No intermediate vertices, shortest path is weight of direct edge
    - Assume W[i,j]=inf if (i,j) does not belong to E
- SP^k+1[i,j] is the minimum of 
    - SP^k[i,j]
    shortest path using only {0,1,...k-1}
    - SP^k[i,k]+SP^k[k,j]
    Combine shortest path from i to k and k to j
- SP^n[i,j]=1 is the length of the shortest path overall from i to j
    - intermediate vertices lie in {0,1,....,n-1}
'''
import numpy as np
def floydwarshall(WMat):
    (rows,cols,x)=WMat.shape
    infinity=np.max(WMat)*rows*rows+1
    SP=np.zeros(shape=(rows,cols,cols+1))
    '''
    - shortest path matrix SP is nxnx(n+1)
    - Initialize SP[i,j,0] to edge weight W(i,j) or inf if no edge
    - Update SP[i,j,k] from SP[i,j,k-1] using the Floyd-Warshall update rule
    - Complexity O(n**3)
    - we only need SP[i,j,k-1] to compute SP[i,j,k]
    - Maintain two slices SP[i,j], SP'[i,j], compute SP' from SP, copy SP' to SP, save space-
    '''
    for i in range(rows):
        for j in range(cols):
            SP[i,j,0]=infinity
    for i in range(rows):
        for j in range(cols):
            if WMat[i,j,0]==1:
                SP[i,j,0]=WMat[i,j,1]
        for k in range(1,cols+1):
            for i in range(rows):
                for j in range(cols):
                    SP[i,j,k]=min(SP[i,j,k-1],SP[i,k-1,k-1]+SP[k-1,j,k-1])
        return (SP[:,:,cols])