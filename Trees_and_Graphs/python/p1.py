from unittest import TestCase, main
from collections import deque


def is_route(graph, node, end, visited=None):
    if visited is None:
        visited = set()

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            if neighbor is end or is_route(graph, neighbor, end, visited):
                return True

    return False


def is_route_bfs(graph, start, end):
    queue = deque(start)
    visited = set()
    while len(queue):
        node = queue.popleft()
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor is not end and neighbor not in visited:
                queue.append(neighbor)
            elif neighbor is end:
                return True
    return False


class Test(TestCase):
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["B", "C"],
        "E": ["C", "F"],
        "F": ["E", "O", "I", "G"],
        "G": ["F", "H"],
        "H": ["G"],
        "I": ["F", "J"],
        "O": ["F"],
        "J": ["K", "L", "I"],
        "K": ["J"],
        "L": ["J"],
        "P": ["Q", "R"],
        "Q": ["P", "R"],
        "R": ["P", "Q"],
    }

    tests = [
        ("A", "L", True),
        ("A", "B", True),
        ("H", "K", True),
        ("L", "D", True),
        ("P", "Q", True),
        ("Q", "P", True),
        ("Q", "G", False),
        ("R", "A", False),
        ("P", "B", False),
    ]

    def test_is_route(self):
        for [start, end, expected] in self.tests:
            actual = is_route(self.graph, start, end)
            assert actual == expected

    def test_is_route_bfs(self):
        for [start, end, expected] in self.tests:
            actual = is_route_bfs(self.graph, start, end)
            assert actual == expected


if __name__ == "__main__":
    main()
