from random import randint, choice

# Global variables
node_count: int = 0  # Keeps track of the number of nodes created
DEPTH: int = 5       # Maximum depth of the generated graph
DEGREE: int = 2      # Maximum number of children a node can have

class Node:
    """
    Represents a node in the graph.
    Each node has a unique ID, a value, and a list of neighbors.
    """
    def __init__(self, value: int, neighbors: list, node_id: int) -> None:
        self.value = value          # Value of the node
        self.neighbors = neighbors  # List of neighbor nodes
        self.id = node_id            # Unique ID of the node

    def __str__(self) -> str:
        """Returns a string representation of the node."""
        n = [n.id for n in self.neighbors]  # Extract neighbor IDs for display
        return f"Node id : {self.id} - value : {self.value} - neighbors : {n}"

def generate_graph(node: Node, threshold: int) -> None:
    """
    Recursively generates a random graph with a given depth threshold.
    Each node is assigned a random number of neighbors (up to DEGREE+1).
    """
    if threshold >= 1:
        # Create a list of uninitialized neighbor slots
        neighbors = [None for _ in range(randint(1, DEGREE + 1))]
        node.neighbors = neighbors
        
        for n in range(len(neighbors)):
            global node_count
            node_count += 1
            # Create a new node with a random value and assign it as a neighbor
            new = Node(value=randint(1, 1000), neighbors=[node], node_id=node_count)
            node.neighbors[n] = new
            # Recursively generate neighbors for the new node
            generate_graph(node=new, threshold=threshold - 1)

def pre_order_visit(node: Node, visited: set = None) -> None:
    """
    Performs a pre-order traversal of the graph and prints each node.
    Keeps track of visited nodes to avoid infinite loops.
    """
    if visited is None:
        visited = set()
    if node.id not in visited:
        visited.add(node.id)
        print(node)
        # Recursively visit all neighbors
        for n in node.neighbors:
            pre_order_visit(node=n, visited=visited)

def find_leaf(node: Node, visited: list = None) -> Node:
    """
    Finds and returns a leaf node (a node with no unvisited neighbors).
    """
    if visited is None:
        visited = []
    visited.append(node)
    
    neighbors: list = []
    for n in node.neighbors:
        if n not in visited:
            neighbors.append(n)
    else:
        if not neighbors:
            return node  # Return the current node if no unvisited neighbors exist
        else:
            return find_leaf(node=choice(neighbors), visited=visited)  # Recursively find a leaf

if __name__ == "__main__":
    # Initialize the graph with a root node
    start_node = Node(randint(1, 1000), [], 1)
    generate_graph(node=start_node, threshold=DEPTH)
    
    # Perform a pre-order traversal of the generated graph
    pre_order_visit(start_node)
    print('*' * 50)
    
    # Find and print a leaf node from the graph
    start_node_2 = find_leaf(start_node)
    print(start_node_2)
