import heapq
import itertools

class TreeNode:
    def __init__(self, data, weight, depth=0):
        self.data = data
        self.weight = weight
        self.depth = depth
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def best_cost_search(root, target_data):
    heap = []
    counter = itertools.count()  # Unique sequence count
    heapq.heappush(heap, (root.weight, 0, next(counter), root))  # (cost, depth, count, node)
    visited = set()

    while heap:
        cost, depth, _, node = heapq.heappop(heap)
        if node.data == target_data:
            node.depth = depth  # Set depth only when found
            return node

        visited.add(node.data)
        for child in node.children:
            if child.data not in visited:
                heapq.heappush(heap, (child.weight + depth + 1, depth + 1, next(counter), child))
    return None

if __name__ == "__main__":
    # Build tree: Root -> 3 children -> each child has 3 children
    root = TreeNode('A', 2)

    # Level 1
    b = TreeNode('B', 3)
    c = TreeNode('C', 1)
    d = TreeNode('D', 5)

    root.add_child(b)
    root.add_child(c)
    root.add_child(d)

    # Level 2 (each has 3 children)
    for idx, parent in enumerate([b, c, d], start=1):
        for j in range(1, 4):  # 3 children for each
            node_label = f"{parent.data}{j}"
            node_weight = j + idx  # Example weight
            child_node = TreeNode(node_label, node_weight)
            parent.add_child(child_node)

    # Search for a node
    result = best_cost_search(root, 'D3')
    if result:
        print(f"Found node: {result.data}, weight: {result.weight}, depth: {result.depth}")
    else:
        print("Node not found.")