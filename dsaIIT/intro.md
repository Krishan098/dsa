# Graph

### G=(V,E)

- V is a set of vertices or nodes
    - one vertex, many vertices
- E is a set of edges
- E belongs to VxV - binary relation

### Directed graph
- (v,v') belongs to E doesnot imply (v',v) belongs to E
### Undirected graph
- (v,v') belongs to E if (v',v) belongs to E
- Effectively (v,v'),(v',v) is the same edge

## Paths
- A path is a sequence of vertices v1,v2,v3.....vk connected by edges
    - For 1<=i<k,(v_i,v_i+1) belongs to E
- Normally, a path does not visit a vertex twice
- a sequence that re-visits a vertex is usually called a walk

## Reachability
- Vertex v is reachable from vertex u if there is a path from u to v.

## MAP Colouring problem

- Assign each state a colour

- States that share a border should be coloured differently

- how many colours do we need

- create a graph
    - each state is a vertex
    - connect states that share a border
- assign colours to nodes so that endpoints of an edge have different colours

- only need the underlying graph

- Abstraction: if we distort the graph, the problem is unchanged

## Graph colouring problem
- graph G =(V,E), set of colours C
- Colouring is a function c: V->C such that (u,v) belongs to E => c(u)!= c(v)
- Planar graph : edges don't cross each other
- Given G=(V,E) what is the smallest set of colours need to colour G
    - Four Colour Theorem for planar graphs derived from geographical maps, 4 colours suffice

## Vertex cover

- A hotel wants to install security cameras
    - all corridors are straight lines
    - Camera can monitor all corridors that meet at an intersection
- min number of cameras needed?
- Represent the floor plan as a graph
    - V -- intersections of corridors 
    - E -- corridor segments connecting intersections
#### Vertex cover
- Marking v coverts all edges from v
- Mark smallest subset of V to cover all edges

### Independent set
- A dance school puts up group dances
    - Each dance has a set of dancers
    - Sets of dancers may overlap across dances
- Organizing a cultural programme 
    - Each dancer performs at most once
    - Maximum numbers of dances possible?
- Represent the dances as a graph
    - V-- dances
    - E-- sets of dancers overlap
##### Independent set
- subset of vertices such that no two are connected by an edge

## Matching

- Class project can be done by one or two people
    - if two people, they must be friends
- Assume we have a graph describing friendships
- Find a good allocation of groups

##### Matching

- G=(V,E) an undirected graph
- A matching is a subset McE of mutually disjoint edges

- Find a maximal matching in G

