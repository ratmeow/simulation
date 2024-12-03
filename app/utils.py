from typing import Optional
from collections import deque
from app.map import Map
import heapq


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
            if (0 <= neighbor[0] < graph.height) and (0 <= neighbor[1] < graph.width) and (
                    neighbor not in visited) and not isinstance(graph.schema[neighbor].get(), obstacle):
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current
    return None


def a_star_retrieve(
        graph: Map,
        start: tuple[int, int],
        desired_object,
        obstacle
) -> Optional[list[tuple[int, int]]]:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def manhattan(a: tuple[int, int], b: tuple[int, int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_set = []
    heapq.heappush(open_set, (0, start))

    g_score = {start: 0}
    parent = {start: None}

    while open_set:
        _, current = heapq.heappop(open_set)
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
            if (
                    0 <= neighbor[0] < graph.height and
                    0 <= neighbor[1] < graph.width and
                    not isinstance(graph.schema[neighbor].get(), obstacle)
            ):
                approx_g_score = g_score[current] + 1
                if neighbor not in g_score or approx_g_score < g_score[neighbor]:
                    g_score[neighbor] = approx_g_score
                    f_score = approx_g_score + manhattan(neighbor, start)
                    heapq.heappush(open_set, (f_score, neighbor))
                    parent[neighbor] = current

    return None
