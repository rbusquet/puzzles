from collections import defaultdict


class Solution:
    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
        queue = list[tuple[int, ...]]()
        paths = set[tuple[int, ...]]()

        for node in range(len(vals)):
            queue.append((node,))
            paths.add((node,))

        while queue:
            path = queue.pop()
            for edge in edges:
                if path[-1] not in edge:
                    continue
                neighbor = edge[0] if path[-1] == edge[1] else edge[1]
                if neighbor in path:
                    continue
                if vals[neighbor] > vals[path[0]]:
                    continue
                new_path = (*path, neighbor)
                reverse = new_path[::-1]
                if vals[neighbor] == vals[path[0]]:  # good path
                    if new_path not in paths and reverse not in paths:
                        paths.add(new_path)
                queue.append(new_path)
        return len(paths)
