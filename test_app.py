import directed_graph as g
import algorithms
import undirected_graph as undg

def print_menu_directed():
    print("1. Read graph from a text file")
    print("2. Save graph into a text file")
    print("3. Generate a graph and save it in a text file")
    print("4. Perform operations on the loaded graph")
    print("5. Print graph")
    print("6. Find the lowest length path between 2 vertices (forward BFS)")
    print("7. Find the lowest length path between 2 vertices (backward BFS)")
    print("0. Exit")
    

def print_menu_undirected():
    print("1. Read graph from a text file")
    print("2. Save graph into a text file")
    print("3. Generate a graph and save it in a text file")
    print("4. Perform operations on the loaded graph")
    print("5. Print graph")
    print("6. Find the lowest length path between 2 vertices (forward BFS)")
    print("7. Find the lowest length path between 2 vertices (backward BFS)")
    print("8. Find the connected components of the graph (DFS)")
    print("9. Find the connected components of the graph (BFS)")
    print("0. Exit")

def print_menu():
    print("1. Directed graph")
    print("2. Undirected graph")
    print("0. Exit")


def print_operations_menu():
    print("-----------(VERTEX OPERATIONS)------------")
    print("1. Check if a vertex belongs to the graph")
    print("2. Add a vertex to the graph")
    print("3. Remove a vertex from the graph")
    print("4. Print the number of vertices")
    print("5. Print the in degree of a vertex")
    print("6. Print the out degree of a vertex")
    print("7. Print the inbound edges of a vertex")
    print("8. Print the outbound edges of a vertex")
    print("------------(EDGE OPERATIONS)-------------")
    print("9. Check if an edge belongs to the graph")
    print("10. Print the cost of a given edge")
    print("11. Add an edge to the graph")
    print("12. Remove an edge from the graph")
    print("13. Print the number of edges")
    print("14. Print all the vertices")
    print("15. Print all the edges")
    print("16. Print all dictionaries")
    print("17. Modify the cost of an edge")
    print("0. Go back to the main menu")


def graph_copy_test():
    # create a graph with 4 vertices and 6 edges
    main_graph = g.DirectedGraph()
    main_graph.addVertex(1)
    main_graph.addVertex(2)
    main_graph.addVertex(3)
    main_graph.addVertex(5)
    main_graph.addEdge(1, 1, 0)
    main_graph.addEdge(2, 1, -2)
    main_graph.addEdge(1, 2, 2)
    main_graph.addEdge(3, 5, 5)
    main_graph.addEdge(2, 5, 7)
    main_graph.addEdge(5, 1, 3)

    # check that the graph is created correctly
    assert (main_graph.getNumEdges() == 6)
    assert (main_graph.getNumVertices() == 4)
    assert (main_graph.getCost(3, 5) == 5)
    assert (main_graph.isEdge(5, 3) == False)
    assert (main_graph.isVertex(2) == True)
    assert (main_graph.isVertex(0) == False)
    assert (main_graph.isVertex(4) == False)

    # create a copy of the graph
    graph_copy = g.copy_graph(main_graph)

    # check that the graph has been copied correctly    
    assert (graph_copy.getNumEdges() == 6)
    assert (graph_copy.getNumVertices() == 4)
    assert (graph_copy.getCost(3, 5) == 5)
    assert (graph_copy.isEdge(5, 3) == False)
    assert (graph_copy.isVertex(2) == True)
    assert (graph_copy.isVertex(0) == False)
    assert (graph_copy.isVertex(4) == False)

    # add a vertex and an edge to the copy
    graph_copy.addVertex(51)
    graph_copy.addEdge(5, 3, -1)

    # check that the changes have applied to the copied graph
    assert (graph_copy.getNumEdges() == 7)
    assert (graph_copy.getNumVertices() == 5)
    assert (graph_copy.isVertex(51) == True)
    assert (graph_copy.isEdge(5, 3) == True)
    assert (graph_copy.getCost(5, 3) == -1)

    # check that the original graph has not been modified
    assert (main_graph.isVertex(51) == False)
    assert (main_graph.isEdge(5, 3) == False)
    assert (main_graph.getNumEdges() == 6)
    assert (main_graph.getNumVertices() == 4)



def process_command_operations(graph: g.DirectedGraph, command: str):
    if command == "1":
        print("What is the vertex number?")
        vertex = int(input(">"))
        if graph.isVertex(vertex):
            print("Vertex", vertex, "belongs to the graph.")
        else:
            print("Specified vertex does not belong to the graph.")

    elif command == "2":
        print("What is the vertex number?")
        vertex = int(input(">"))
        graph.addVertex(vertex)

    elif command == "3":
        print("What is the vertex number?")
        vertex = int(input(">"))
        graph.removeVertex(vertex)

    elif command == "4":
        print("The number of vertices in the graph is:", graph.getNumVertices())

    elif command == "5":
        print("What is the vertex number?")
        vertex = int(input(">"))
        print("The in degree of vertex", vertex, "is:", graph.inDegree(vertex))

    elif command == "6":
        print("What is the vertex number?")
        vertex = int(input(">"))
        print("The out degree of vertex", vertex, "is:", graph.outDegree(vertex))

    elif command == "7":
        print("What is the vertex number?")
        vertex = int(input(">"))
        print("The inbound edges of vertex", vertex, "are:")
        for y in graph.getPredecessors(vertex):
            print("(",y, ",", vertex,")")

    elif command == "8":
        print("What is the vertex number?")
        vertex = int(input(">"))
        print("The outbound edges of vertex", vertex, "are:")
        for y in graph.getSuccessors(vertex):
            print("(",vertex, ",", y,")")

    elif command == "9":
        print("What are the vertices of the edge?")
        x = int(input("x = "))
        y = int(input("y = "))
        if graph.isEdge(x, y):
            print("The edge belongs to the graph.")
        else:
            print("Specified edge does not belong to the graph.")

    elif command == "10":
        print("What are the vertices of the edge?")
        x = int(input("x = "))
        y = int(input("y = "))
        print("The cost of specified edge is:", graph.getCost(x, y))

    elif command == "11":
        print("What are the vertices of the edge?")
        x = int(input("x = "))
        y = int(input("y = "))
        cost = int(input("cost = "))
        graph.addEdge(x, y, cost)
        print("Edge has been successfully added.")

    elif command == "12":
        print("What are the vertices of the edge?")
        x = int(input("x = "))
        y = int(input("y = "))
        graph.removeEdge(x, y)
        print("Edge has been successfully removed.")

    elif command == "13":
        print("The number of edges in the graph is:", graph.getNumEdges())

    elif command == "14":
        vert = ""
        for x in graph.getVertices():
            vert += (str(x))
            vert += (" ")

        print("Vertices of the graph: ", vert)

    elif command == "15":
        edge = ""
        for x in graph.getEdges():
            edge += (str(x))
            edge += (" ")

        print("Edges of the graph: ", edge)

    elif command == "16":
        print("vIn dictionary:",graph.vIn)
        print("vOut dictionary:",graph.vOut)
        print("edges dictionary:",graph.edges)

    elif command == "17":
        print("What are the vertices of the edge?")
        x = int(input("x = "))
        y = int(input("y = "))
        if graph.isEdge(x, y):
            cost = int(input("cost = "))
            graph.modifyEdge(x, y, cost)
        else:
            print("Specified edge does not belong to the graph.")

    elif command == "0":
        return False
    else:
        print("Wrong input! Please try again.")

    return True


def process_command_main_directed(graph: g.DirectedGraph, command: str):
    if command == "1":
        print("What is the name of the file?")
        filename = input(">")
        graph = g.read_graph(graph, filename)

    elif command == "2":
        print("What is the name of the file?")
        filename = input(">")
        g.save_graph(graph, filename)

    elif command == "3":
        print("What is the name of the file?")
        filename = input(">")
        print("What is the number of vertices?")
        num_v = int(input(">"))
        print("What is the number of edges?")
        num_e = int(input(">"))

        gen_graph = g.generate_graph(num_v, num_e)
        g.save_graph(gen_graph, filename)

    elif command == "4":
        keep_running = True
        while keep_running:
            print_operations_menu()
            command = input(">")

            keep_running = process_command_operations(graph, command)
            print("")

    elif command == "5":
        g.print_graph(graph)

    elif command == "6":
        x = int(input("source = "))
        y = int(input("destination = "))
        if not graph.isVertex(x) or not graph.isVertex(y):
            print("The vertices do not belong to the graph.")

        path, length = algorithms.shortest_path(graph, x, y)
        if path == None:
            print("There is no path between the two vertices")
        else:
            print("Found path with length", length, ":", path)

    elif command == "7":
        x = int(input("source = "))
        y = int(input("destination = "))
        if not graph.isVertex(x) or not graph.isVertex(y):
            print("The vertices do not belong to the graph.")

        path, length = algorithms.shortest_path_r(graph, x, y)
        if path == None:
            print("There is no path between the two vertices")
        else:
            print("Found path with length", length, ": ", path)

    elif command == "0":
        return graph, False
    else:
        print("Wrong input! Please try again.")

    return graph, True

def process_command_main_undirected(graph: undg.UndirectedGraph, command: str):
    if command == "1":
        print("What is the name of the file?")
        filename = input(">")
        graph = undg.read_graph(graph, filename)

    elif command == "2":
        print("What is the name of the file?")
        filename = input(">")
        undg.save_graph(graph, filename)

    elif command == "3":
        print("What is the name of the file?")
        filename = input(">")
        print("What is the number of vertices?")
        num_v = int(input(">"))
        print("What is the number of edges?")
        num_e = int(input(">"))

        gen_graph = undg.generate_graph(num_v, num_e)
        undg.save_graph(gen_graph, filename)

    elif command == "4":
        keep_running = True
        while keep_running:
            print_operations_menu()
            command = input(">")

            keep_running = process_command_operations(graph, command)
            print("")

    elif command == "5":
        undg.print_graph(graph)

    elif command == "6":
        x = int(input("source = "))
        y = int(input("destination = "))
        if not graph.isVertex(x) or not graph.isVertex(y):
            print("The vertices do not belong to the graph.")

        path, length = algorithms.shortest_path(graph, x, y)
        if path == None:
            print("There is no path between the two vertices")
        else:
            print("Found path with length", length, ":", path)

    elif command == "7":
        x = int(input("source = "))
        y = int(input("destination = "))
        if not graph.isVertex(x) or not graph.isVertex(y):
            print("The vertices do not belong to the graph.")

        path, length = algorithms.shortest_path_r(graph, x, y)
        if path == None:
            print("There is no path between the two vertices")
        else:
            print("Found path with length", length, ": ", path)

    elif command == "8":
        algorithms.print_connected_comps(algorithms.connected_dfs_undirected(graph))

    elif command == "9":
        algorithms.print_connected_comps(algorithms.connected_bfs_undirected(graph))

    elif command == "0":
        return graph, False
    else:
        print("Wrong input! Please try again.")

    return graph, True

def main():
    graph_copy_test()
    main_graph = g.DirectedGraph()
    main_graph = g.read_graph(main_graph, "input_graph.txt")

    main_graph_undir = undg.UndirectedGraph()
    main_graph_undir = undg.read_graph(main_graph_undir, "input_graph_undirected.txt")

    keep_running = True
    while keep_running:
        try:
            print_menu()
            command = input(">")

            if(command == "1"):
                keep_submenu_open = True
                while keep_submenu_open:
                    print_menu_directed()
                    command = input(">")
                    main_graph, keep_submenu_open = process_command_main_directed(main_graph, command)
                    print("")

            elif(command == "2"):
                keep_submenu_open = True
                while keep_submenu_open:
                    print_menu_undirected()
                    command = input(">")
                    main_graph_undir, keep_submenu_open = process_command_main_undirected(main_graph_undir, command)
                    print("")

            elif command == "0":
                keep_running = False

            print("")

        except Exception as e:
            print(e, "\n")

if __name__ == "__main__":
    main()