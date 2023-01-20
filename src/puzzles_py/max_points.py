from fractions import Fraction
from itertools import combinations


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) == 1:
            return 1
        if len(points) == 2:
            return 2
        lines = []
        for p1, p2 in combinations(points, 2):
            x1, y1 = p1
            x2, y2 = p2

            if x2 == x1:
                # avoid division by 0
                a = float("inf")  # placeholder
                b = Fraction(x1, 1)
                lines.append((a, b))
                continue
            # slope: y2 - y1/x2-x1
            a = Fraction(y2 - y1, x2 - x1)  # type: ignore
            # y = mx + b
            # b = y - ax
            b = y1 - a * x1  # type: ignore
            lines.append((a, b))

        max_in_line = 0
        for a, b in lines:
            in_line = 0
            for x, y in points:
                if a == float("inf"):
                    in_line += x == b
                elif a * x + b == y:
                    in_line += 1
            if in_line > max_in_line:
                max_in_line = in_line
        return max_in_line


Solution().maxPoints([[-6, -1], [3, 1], [12, 3]])
