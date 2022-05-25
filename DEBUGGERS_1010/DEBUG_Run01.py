"""
* Insert program documentation here *
"""
import sys
import collections
from heapq import heappush, heappop


class Node:
    """
    ***
    param: edges --> edges are the links between the adjacent nodes, a node
    will store a list of all the edges leading from itself.
    """

    def __init__(self, name):
        self.data = (sys.maxsize, self)
        self.name = name
        self.parent = None
        self.edges = []
        self.used = False
        self.is_on_open_list = False  # Boolean specifying whether the node is
        # on the open list, preventing us adding it twice

    # Add an edge from the list of edges from this node
    def add_edge(self, edge):
        self.edges.append(edge)

    def __lt__(self, other):
        """
        This magic method will compare the nodes by name; and this
        is to deal with an issue with the priority queue in which the issue is:
        when comparing values, the queue will compare both
        the distance and the Node in the tuple and Nodes
        cannot by default be compared.  (This is so that the priority
        queue knows how to order the data if the distances are equal.)
        """
        return self.name < other.name


class Edge:
    def __init__(self, StartNode, EndNode, Distance):
        self.startnode = StartNode
        self.endnode = EndNode
        self.dist = Distance


class Graph:
    def add_edge(self, Start, End, distance):
        """
        Create an edge using the two nodes: StartNode and EndNode
        and the distance passed in
        first create an Edge going from the start
        to end and add it to the start node's edges.
        then create an Edge going from the end to
        start and add it to the end node's edges.
        This way you have a two-way connection between nodes
        which will be more efficient.
        *param* : Start --> represents the start Node
        *param* : End --> represents the end node
        """
        forwardedge = Edge(Start, End, distance)
        backwardedge = Edge(End, Start, distance)
        Start.add_edge(forwardedge)
        End.add_edge(backwardedge)

    # Actually do the Dijkstra's algorithm
    def dijkstra(self, start, end):
        current_node = start
        open_list = []

        start.data = (0, start)
        heappush(open_list, start.data)

        while current_node != end and len(open_list) > 0:
            for i in range(0, (len(current_node.edges))):
                if not current_node.edges[i].endnode.used:
                    # NEED TO ADD A CHECK FOR THE NODE TO PREVENT IT BEING ADDED TWICE
                    if not current_node.edges[i].endnode.is_on_open_list:
                        heappush(open_list, current_node.edges[i].endnode.data)
                        current_node.edges[i].endnode.is_on_open_list = True

                if current_node.edges[i].endnode.data[0] > current_node.edges[i].dist + current_node.data[0]:
                    current_node.edges[i].endnode.parent = current_node
                    current_node.edges[i].endnode.data = (current_node.edges[i].dist + current_node.data[0],
                                                          current_node.edges[i].endnode)
            current_node.used = True
            return_tuple = heappop(open_list)
            current_node = return_tuple[1]
            print(current_node.name)
        route = collections.deque([])
        while current_node is not None:
            route.appendleft(current_node.name)  # Add to the left of the queue
            current_node = current_node.parent
        return route


# FUNCTION CALLS HERE:
Amsterdam = Node("Amsterdam")
Brussels = Node("Brussels")
Cologne = Node("Cologne")
Frankfurt = Node("Frankfurt")
London = Node("London")
Munich = Node("Munich")
Paris = Node("Paris")
Stuttgart = Node("Stuttgart")

newGraph = Graph()
newGraph.add_edge(Amsterdam, Cologne, 263)
newGraph.add_edge(Amsterdam, Brussels, 211)
newGraph.add_edge(Brussels, Cologne, 211)
newGraph.add_edge(Cologne, Frankfurt, 190)
newGraph.add_edge(Frankfurt, Munich, 393)
newGraph.add_edge(Stuttgart, Munich, 221)
newGraph.add_edge(Frankfurt, Stuttgart, 207)
newGraph.add_edge(London, Brussels, 370)
newGraph.add_edge(London, Paris, 461)
newGraph.add_edge(Paris, Brussels, 305)
newGraph.add_edge(Paris, Frankfurt, 572)
newGraph.add_edge(Paris, Stuttgart, 624)

# Calculate the shortest distance
returned_route = newGraph.dijkstra(London, Munich)
print(returned_route)
