from collections import Counter
from unittest import TestCase, main


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)

        count = 1
        last = prev[0]
        result = ""
        for ch in prev[1:]:
            if ch == last:
                count += 1
            else:
                result += f"{count}{last}"
                last = ch
                count = 1

        result += f"{count}{last}"
        return result


class TestCountAndSay(TestCase):
    def test_is_correct(self) -> None:
        solution = Solution()

    def test_1(self):
        self.assertEqual(Solution().countAndSay(1), "1")

    def test_2(self):
        self.assertEqual(Solution().countAndSay(2), "11")

    def test_3(self):
        self.assertEqual(Solution().countAndSay(3), "21")

    def test_4(self):
        self.assertEqual(Solution().countAndSay(4), "1211")

    def test_5(self):
        self.assertEqual(Solution().countAndSay(5), "1211")

    def test_6(self):
        self.assertEqual(Solution().countAndSay(6), "1211")

    def test_7(self):
        self.assertEqual(Solution().countAndSay(7), "1211")

    def test_8(self):
        self.assertEqual(Solution().countAndSay(8), "1211")


if __name__ == "__main__":
    main()
