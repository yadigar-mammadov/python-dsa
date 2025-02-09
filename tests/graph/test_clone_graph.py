from typing import Optional

import pytest
from algorithms.graph.clone_graph import CloneGraph
from algorithms.graph.clone_graph import Node
from collections import deque

@pytest.mark.parametrize(
    "node_edges",
    [
        ([[2,4],[1,3],[2,4],[1,3]]),
        ([[2],[1,3],[2]]),
        ([[]]),
        ([])
    ]
)
def test_clone_graph(node_edges):
    node = create_node(node_edges)
    cloneGraph = CloneGraph(node)
    clone_by_bfs = cloneGraph.clone_using_bfs()
    clone_by_dfs = cloneGraph.clone_using_dfs()
    assert compare_nodes(clone_by_bfs, node)
    assert compare_nodes(clone_by_dfs, node)

def create_node(node_edges: list) ->Optional[Node]:
    nodes = [Node(n) for n in range(len(node_edges))]
    if len(nodes) == 0:
        return None
    for key, edges in enumerate(node_edges):
        for edge in edges:
            nodes[key].neighbors.append(nodes[edge-1])
    return nodes[0]

def compare_nodes(clone: Optional[Node], expected: Optional[Node] ) -> bool:
    if not clone or not expected:
        return not clone and not expected

    queueClone = deque([clone])
    queueExpected = deque([expected])

    visitedClone = {clone.val: True}
    visitedExpected = {expected.val: True}

    while queueClone:
        elClone = queueClone.popleft()
        elExpected = queueExpected.popleft()
        if not elExpected or elClone.val != elExpected.val:
            return False
        for n in elClone.neighbors:
            if n.val not in visitedClone:
                visitedClone[n.val] = True
                queueClone.append(n)
        for n in elExpected.neighbors:
            if n.val not in visitedExpected:
                visitedExpected[n.val] = True
                queueExpected.append(n)
    return True








