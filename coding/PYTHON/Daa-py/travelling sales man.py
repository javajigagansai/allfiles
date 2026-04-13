import sys
def totalCost(mask, pos, n, cost):
    if mask == (1 << n) - 1:
        return cost[pos][0]
    ans = sys.maxsize
    for i in range(n):
        if (mask & (1 << i)) == 0:
            ans = min(ans, cost[pos][i] +totalCost(mask | (1 << i), i, n, cost))
    return ans
def tsp(cost):
    n = len(cost)
    return totalCost(1, 0, n, cost)
if __name__ == "__main__":
    cost = [[0, 10, 15, 20],[10, 0, 35, 25],[15, 35, 0, 30],[20, 25, 30, 0]]
    result = tsp(cost)
    print(result)