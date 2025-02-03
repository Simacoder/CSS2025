from collections import deque

def bfs_shortest_path(graph, start, goal):

    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return None

def main():
    example_graph  = {
        "A" : ["B", "C"],
        "B" : ["A", "D", "E"],
        "C" : ["A", "F"],
        "D" : ["B"],
        "E" : ["B", "F"],
        "F" : ["C", "E"]
    }

    start_node = "A"
    goal_node = "F"
    path = bfs_shortest_path(example_graph, start_node, goal_node)
    if path:
        print(f"shortest path from {start_node} to {goal_node} : {path}")
    else:
        print(f"No path found....")

if __name__ == "__main__":
    main()