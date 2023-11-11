class Solution20:

    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                result.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return result
