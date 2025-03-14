class BacktrackingSearch:
    def __init__(self, graph):
        self.graph = graph  # Adjacency list representation of the graph
        self.path = []  # Stores the current path

    def backtrack(self, node):
        """ Recursive function to perform backtracking search """
        self.path.append(node)  # Add current node to path
        print("Current Path:", " -> ".join(self.path))  # Print traversal path

        # If it's a leaf node, backtrack
        if node not in self.graph or not self.graph[node]:
            self.path.pop()  # Remove the leaf node and backtrack
            return

        # Explore each child node
        for child in self.graph[node]:
            self.backtrack(child)  # Recursive call to traverse deeper

        # Backtrack from current node after exploring all children
        self.path.pop()

# Define the given graph (Figure 3.29) as an adjacency list
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'I'],
    'E': ['J'],
    'F': ['K', 'L'],
    'G': ['M', 'N'],
    'H': ['O', 'P'],
    'I': ['R']
}

# Initialize the backtracking search
backtracking_search = BacktrackingSearch(graph)
print("Backtracking Traversal Starting from A:\n")
backtracking_search.backtrack('A')
