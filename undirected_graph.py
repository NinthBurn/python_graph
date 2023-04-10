import directed_graph as dg
import algorithms
import random
import os

class UndirectedGraph(dg.DirectedGraph):
    def __init__(self):
        super().__init__()

    # Returns the number of edges in a graph
    def getNumEdges(self):
        return len(self.getEdges())//2

    # Removes a vertex from the graph
    def removeVertex(self, x):
        if self.isVertex(x):
            for y in self.getPredecessors(x):
                self.removeEdge(y, x)

            self.vIn.pop(x)
            self.vOut.pop(x)
        else:
            raise Exception("Vertex does not belong to the graph")

    # Adds an edge to the graph
    def addEdge(self, x, y, cost):
        if not self.isVertex(x) or not self.isVertex(y):
            raise Exception("Vertices do not belong to the graph")

        if not self.isEdge(x, y):
            self.vOut[x].append(y)
            self.vIn[x].append(y)
            self.vIn[y].append(x)
            self.vOut[y].append(x)
            self.edges[(x, y)] = cost
            self.edges[(y, x)] = cost
        else: raise Exception("Edge already exists")

    def modifyEdge(self, x, y, cost):
        if not self.isVertex(x) or not self.isVertex(y):
            raise Exception("Vertices do not belong to the graph")
        
        if not self.isEdge(x, y):
            raise Exception("Edge does not exist")
        else:
            self.edges[(x, y)] = cost
            self.edges[(y, x)] = cost

    # Removes an edge from the graph
    def removeEdge(self, x, y):
        if self.isEdge(x, y):
            self.vOut[x].remove(y)
            self.vIn[x].remove(y)

            self.vOut[y].remove(x)
            self.vIn[y].remove(x)
            self.edges.pop((x, y))
            self.edges.pop((y, x))
        else:
            raise Exception("Edge does not belong to the graph")


# Reads a graph from a specified text file. We assume the data is correct.
def read_graph(graph: UndirectedGraph, filename: str):
    new_graph = UndirectedGraph()
    if not os.path.exists(filename):
        print("File does not exist.")
        return graph

    fp = open(filename, "r")
    lines = fp.readlines()
    line = str(lines[0])
    nline = line.split()
    # number of vertices
    n = int(nline[0])
    # number of edges
    m = int(nline[1])
    i = 0

    for line in lines:
        if i == 0:
            i = 1
            continue

        nline = line.split(" ")
        x, y = int(nline[0]), int(nline[1])
		
        if not new_graph.isVertex(x):
            new_graph.addVertex(x)

        if y != -1:
            cost = int(nline[2])
            if not new_graph.isVertex(y):
                new_graph.addVertex(y)

            new_graph.addEdge(x, y, cost)

    fp.close()
    
    print("Graph has been read successfully.")

    # add isolated vertices
    vert_remaining = n - new_graph.getNumVertices()
    for x in range(0, n):
        if vert_remaining == 0:
            break

        if not new_graph.isVertex(x):
            new_graph.addVertex(x)
            vert_remaining -= 1
        
    return new_graph


# Writes the graph's data to a specified text file.
def save_graph(graph: UndirectedGraph, filename: str):
    fp = open(filename, "w")
    line = str(graph.getNumVertices()) + " " + str(graph.getNumEdges()) + "\n"
    fp.write(line)

    for x in graph.getVertices():
        if graph.inDegree(x) == 0 and graph.outDegree(x) == 0:
            line = str(x) + " -1\n"
            fp.write(line)
        
        for y in graph.getSuccessors(x):
            if y > x: 
                line = str(x) + " " + str(y) + " " + str(graph.getCost(x, y)) + "\n"
                fp.write(line)


# Returns a graph generated according to the requirements.
def generate_graph(num_vertices: int, num_edges: int):
    new_graph = UndirectedGraph()
    min_cost = -3
    max_cost = 11
    num_generated_edges = 0
    temp_edge_dict = {}

    # Validate parameters
    if num_vertices < 0 or num_edges < 0:
        raise Exception("Invalid parameters")

    # Make sure the number of edges doesn't exceed the maximum that is possible for n vertices
    if num_edges > num_vertices * (num_vertices - 1) // 2:
        num_edges = num_vertices * (num_vertices - 1) // 2

    # add all the vertices
    for x in range(0, num_vertices):
        new_graph.addVertex(x)

    # generate all the possible edges
    for i in range(0, num_vertices):
        for j in range(i+1, num_vertices):
            temp_edge_dict[(i, j)] = random.randint(min_cost, max_cost)

    # select num_edges of them and register them in the generated graph
    for i in range(0, num_edges):
        edge = random.choice(list(temp_edge_dict.keys()))
        x, y = edge[0], edge[1]
        new_graph.addEdge(x, y, temp_edge_dict[edge])
        temp_edge_dict.pop(edge)

    return new_graph


# Prints a given graph to the terminal.
def print_graph(graph: UndirectedGraph):
    print(graph.getNumVertices(), graph.getNumEdges())

    for x in graph.getVertices():
        for y in graph.getSuccessors(x):
            if y > x:
                print("Edge going from", x, "to", y, "having cost", graph.getCost(x, y))


