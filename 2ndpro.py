import sys
sys.setrecursionlimit(10000)

def worth_value(s):
    return sum(ord(ch) - ord('a') + 1 for ch in s)

def solve():
    # Input
    N, M = map(int, input().split())
    strings = input().split()
    costs = list(map(int, input().split()))
    
    # Precompute worths
    worths = [worth_value(s) for s in strings]
    
    # Map string -> index
    idx = {s: i for i, s in enumerate(strings)}
    
    # Conflict matrix
    conflict = [[False]*N for _ in range(N)]
    for _ in range(M):
        a, b = input().split()
        i, j = idx[a], idx[b]
        conflict[i][j] = conflict[j][i] = True
    
    budget = int(input().strip())
    
    # DP: dp[i][b] = max worth using first i items with budget b
    dp = [[-1]*(budget+1) for _ in range(N+1)]
    
    def knapsack(i, b, chosen):
        if i == N:
            return 0
        if dp[i][b] != -1:
            return dp[i][b]
        
        # Option 1: skip
        res = knapsack(i+1, b, chosen)
        
        # Option 2: take (if no conflict and enough budget)
        if costs[i] <= b:
            can_take = True
            for c in chosen:
                if conflict[i][c]:
                    can_take = False
                    break
            if can_take:
                res = max(res, worths[i] + knapsack(i+1, b-costs[i], chosen+[i]))
        
        dp[i][b] = res
        return res
    
    print(knapsack(0, budget, []))

# Run
if __name__ == "__main__":
    solve()
