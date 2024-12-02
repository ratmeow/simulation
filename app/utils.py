from typing import Optional
from collections import deque
from app.map import Map


def bfs_retrieve(graph: Map,
                 start: tuple[int, int],
                 desired_object,
                 obstacle) -> Optional[list[tuple]]:

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = set()
    visited.add(start)

    parent = {start: None}

    while queue:
        current = queue.popleft()
        x, y = current

        if isinstance(graph.schema[current].get(), desired_object):
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            if (0 <= neighbor[0] < graph.height) and (0 <= neighbor[1] < graph.weight) and (
                    neighbor not in visited) and not isinstance(graph.schema[neighbor].get(), obstacle):
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current
    return None
