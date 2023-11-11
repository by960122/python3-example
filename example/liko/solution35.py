class Solution35:
    def countAndSay(self, n: int) -> str:
        prev = "1"
        for index in range(n - 1):
            curr = ""
            start = 0
            pos = 0
            while pos < len(prev):
                while pos < len(prev) and prev[pos] == prev[pos]:
                    pos += 1
                curr += str(pos - start) + prev[start]
                start = pos
            prev = curr
        return prev
