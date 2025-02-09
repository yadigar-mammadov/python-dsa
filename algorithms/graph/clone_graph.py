from typing import Optional
from collections import deque, defaultdict

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class CloneGraph:
    def __init__(self,  node: Optional[Node]):
        self.node = node
        self.visited = {}

    def clone_using_dfs(self) -> Optional[Node]:
        return self.dfs(self.node)

    def dfs(self, node: Optional[Node]) ->Optional[Node]:
        if not node: return node

        if node.val in self.visited:
            return self.visited[node.val]

        self.visited[node.val] = Node(node.val)

        for n in node.neighbors:
            if n.val in self.visited:
                self.visited[node.val].neighbors.append(self.visited[n.val])
            else:
                self.visited[node.val].neighbors.append(self.dfs(n))
        return self.visited[node.val]

    def clone_using_bfs(self) -> Optional[Node]:
        if not self.node: return self.node
        queue = deque([self.node])
        visited = {self.node.val: Node(self.node.val)}

        while queue:
            el = queue.popleft()
            for n in el.neighbors:
                if n.val not in visited:
                    queue.append(n)
                    visited[n.val] = Node(n.val)
                visited[el.val].neighbors.append(visited[n.val])

        return visited[self.node.val]




