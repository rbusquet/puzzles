from collections import Counter
from heapq import heappop, heappush


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        frequencies = Counter(arr)
        frequencies.most_common()
