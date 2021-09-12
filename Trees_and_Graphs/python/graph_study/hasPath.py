from unittest import TestCase
from collections import deque


def has_path_bfs(graph: dict, source: str, destination: str):
    queue = deque([source])

    while len(queue):
        node = queue.popleft()

        if node == destination:
            return True
        for neighbor in graph[node]:
            queue.append(neighbor)

    return False


def has_path_dfs(graph: dict, source: str, destination: str):
    if source == destination:
        return True

    for neighbor in graph[source]:
        if has_path_dfs(graph, neighbor, destination):
            return True

    return False


def has_path_dfs_stack(graph: dict, source: str, destination: str):
    stack = [source]

    while len(stack):
        node = stack.pop()
        if node == destination:
            return True
        for neighbor in graph[node]:
            stack.append(neighbor)

    return False


class hasPath(TestCase):

    def setUp(self) -> None:
        self.graph = dict(f=['g', 'i'], g=['h'], h=[], i=['g', 'k'], j=['i'], k=[])

        self.testCases = [['f', 'k', True],
                          ['f', 'h', True],
                          ['f', 'j', False],
                          ['j', 'h', True] ]

    def test_has_path_bfs(self):
        for source, destination, result in self.testCases:
            if result:
                assert has_path_bfs(self.graph, source, destination), result
            else:
                self.assertFalse(has_path_bfs(self.graph, source, destination), result)

    def test_has_path_dfs(self):
        for source, destination, result in self.testCases:
            if result:
                assert has_path_dfs(self.graph, source, destination), result
            else:
                self.assertFalse(has_path_dfs(self.graph, source, destination), result)

    def test_has_path_dfs_stack(self):
        for source, destination, result in self.testCases:
            if result:
                assert has_path_dfs_stack(self.graph, source, destination), result
            else:
                self.assertFalse(has_path_dfs_stack(self.graph, source, destination), result)
