class Graph:
    def __init__(self):
        # Dictionary to store the graph
        self.graph = {}

    def add_vertex(self, vertex):
        # Add a vertex if it doesn't already exist
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        # Add an edge from one vertex to another
        if from_vertex not in self.graph:
            self.add_vertex(from_vertex)
        if to_vertex not in self.graph:
            self.add_vertex(to_vertex)
        self.graph[from_vertex].append(to_vertex)

    def dfs(self, start_vertex, visited=None):
        # Initialize visited set during the first call
        if visited is None:
            visited = set()

        # Mark the current vertex as visited
        visited.add(start_vertex)
        print(start_vertex, end=" ")

        # Recur for all adjacent vertices not visited yet
        for neighbor in self.graph[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def display_dfs(self, start_vertex):
        print("DFS Traversal:")
        self.dfs(start_vertex)
        print()  # New line after traversal


# Example usage
g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")
g.add_edge("D", "E")
g.add_edge("E", "F")
g.add_edge("F", "C")  # Creates a cycle

g.display_dfs("A")
