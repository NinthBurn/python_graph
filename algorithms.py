import directed_graph as g

# Finds the shortest walk from vertex s to vertex d in a graph g.
# Returns the list of vertices along the walk + the length. Returns None if d is not accessible from s.
def shortest_path(graph: g.DirectedGraph, src, dest):
    parent, children, dist = bfs(graph, src)
    walk = []

    # dest is unreachable from src
    if dest not in parent:
        return None, -1
    
    # start from dest, and go through each of the parents back to the root/src
    current_node = dest
    while current_node != src:
        walk.append(current_node)
        current_node = parent[current_node]

    walk.append(src)
    walk.reverse()
    return walk, dist[dest]


# Finds a walk from vertex s to vertex d in a graph g using DFS. 
def find_path_dfs(graph: g.DirectedGraph, src, dest):
    parent, children, dist = dfs(graph, src)
    walk = []

    # dest is unreachable from src
    if dest not in parent:
        return None, -1
    
    # start from dest, and go through each of the parents back to the root/src
    current_node = dest
    while current_node != src:
        walk.append(current_node)
        current_node = parent[current_node]

    walk.append(src)
    walk.reverse()
    return walk


# Executes Breadth-First Search in graph g starting from vertex s.
# Returns 3 dictionaries:
#   * the first is a dictionary mapping each accessible vertex to its parent
#   * the second is a dictionary mapping each accessible vertex to the list of its children
#   * the third is a dictionary mapping each accessible vertex to the distance from s to it

def bfs(graph: g.DirectedGraph, src):
    parent = {}
    children = {}
    dist = {}

    parent[src] = None
    children[src] = []
    dist[src] = 0

    queue = [src]
    visited = {}
    visited[src] = 0
    # visited = [src]

    while len(queue) > 0:
        current_node = queue.pop(0)

        # for x in graph.getSuccessors(current_node):
        for x in graph.vOut[current_node]:
            # if node was not visited, add it to the queue
            if x not in visited:
                children[x] = []
                parent[x] = current_node
                dist[x] = dist[current_node] + 1
                
                visited[x] = 0
                # visited.append(x)
                queue.append(x)
                children[current_node].append(x)

    return parent, children, dist


# Executes Backward Breadth-First Search in graph g starting from vertex s.
# Returns 2 dictionaries:
#   * the first is a dictionary mapping each accessible vertex to a child vertex (next)
#   * the second is a dictionary mapping each accessible vertex to the distance from s to it
def rbfs(graph: g.DirectedGraph, src):
    child = {}
    dist = {}

    child[src] = None
    dist[src] = 0

    queue = [src]
    visited = {}
    visited[src] = 0

    while len(queue) > 0:
        current_node = queue.pop(0)

        for x in graph.vIn[current_node]:
            # if node was not visited, add it to the queue
            if x not in visited:
                child[x] = current_node
                dist[x] = dist[current_node] + 1
                
                # mark node as visited
                visited[x] = 0
                queue.append(x)

    return child, dist


# Executes Depth-First Search in graph g starting from vertex s.
# Returns 3 dictionaries:
#   * the first is a dictionary mapping each accessible vertex to its parent
#   * the second is a dictionary mapping each accessible vertex to the list of its children
#   * the third is a dictionary mapping each accessible vertex to the distance from s to it

def dfs(graph: g.DirectedGraph, src):
    parent = {}
    children = {}
    dist = {}

    parent[src] = None
    children[src] = []
    dist[src] = 0

    stack = [src]
    visited = {}
    visited[src] = 0

    while len(stack) > 0:
        current_node = stack.pop()

        for x in graph.getSuccessors(current_node):
            # if node was not visited, add it on the stack
            if x not in visited:
                children[current_node].append(x)
                children[x] = []
                parent[x] = current_node
                dist[x] = dist[current_node] + 1
                
                visited[x] = 0
                stack.append(x)

    return parent, children, dist


# Returns a list with all the connected components of an undirected graph, using BFS algorithm.
def connected_bfs_undirected(graph: g.DirectedGraph):
    # get a list with all the vertices
    vertices = graph.getVertices()
    connected_components = []

    # for each vertex, find the connected component it belongs to
    while len(vertices) > 0:
        x = vertices[0]
        
        # get the set of vertices forming a connected component using BFS
        component, c1, c2 = bfs(graph, x)

        # save it
        connected_components.append(component)

        # remove the vertices for which we already have found their connected component
        for vertex in component:
            vertices.remove(vertex)

    return connected_components

        
# Returns a list with all the connected components of an undirected graph, using DFS algorithm.
def connected_dfs_undirected(graph: g.DirectedGraph):
    vertices = graph.getVertices()
    connected_components = []

    # for each vertex, find the connected component it belongs to
    while len(vertices) > 0:
        x = vertices[0]
        
        # get the set of vertices forming a connected component
        component, c1, c2 = dfs(graph, x)

        # save it
        connected_components.append(component)

        # remove the vertices for which we already have found their connected component
        for vertex in component:
            vertices.remove(vertex)

    return connected_components


# A print function for each connected component.
def print_connected_comps(connected_components):
    for component in connected_components:
        result = ""
        for vertex in component:
            result += str(vertex) + " "
        print("Connected component containing the vertices", result)


# Finds the shortest walk from vertex s to vertex d in a graph g, using a backward breadth-first search.
# Returns the list of vertices along the walk. Returns None if d is not accessible from s.
def shortest_path_r(graph: g.DirectedGraph, src, dest):
    next, dist = rbfs(graph, dest)
    walk = []

    # dest is unreachable from src
    if src not in next:
        return None, -1
    
    # start from dest, and go through each of the parents back to the root/src
    current_node = src
    while current_node != dest:
        walk.append(current_node)
        current_node = next[current_node]

    walk.append(dest)

    return walk, dist[src]
	
