class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        # Total path length must be even
        if (m + n - 1) % 2 != 0:
            return False

        # First must be '(' and last must be ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        # dp[i][j] = set of possible balances at (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]

        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                change = 1 if grid[i][j] == '(' else -1

                # Get possible balances from top and left
                prev = set()

                if i > 0:
                    prev.update(dp[i - 1][j])

                if j > 0:
                    prev.update(dp[i][j - 1])

                for balance in prev:
                    new_balance = balance + change

                    # Balance can never become negative
                    if new_balance < 0:
                        continue

                    # Remaining cells after current cell
                    remaining = (m - 1 - i) + (n - 1 - j)

                    # We need enough ')' to bring balance back to 0
                    if new_balance > remaining:
                        continue

                    dp[i][j].add(new_balance)

                # Optional early exit
                if not dp[i][j]:
                    continue

        return 0 in dp[m - 1][n - 1]