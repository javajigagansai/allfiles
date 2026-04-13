import random
import math
from itertools import permutations
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Swap with last element
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def randomized_quick_sort(arr, low, high):
    if low < high:
        pivot = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pivot - 1)
        randomized_quick_sort(arr, pivot + 1, high)
def quick_sort(arr):
    randomized_quick_sort(arr, 0, len(arr) - 1)
    return arr
def vertex_cover_approx(graph):
    cover = set()
    edges = set()
    for u in graph:
        for v in graph[u]:
            edges.add((u, v))
    while edges:
        u, v = edges.pop()
        cover.add(u)
        cover.add(v)
        edges = {e for e in edges if u not in e and v not in e}
    return cover
def tsp_dynamic_programming(graph):
    n = len(graph)
    dp = [[None] * (1 << n) for _ in range(n)]
    def tsp(mask, pos):
        if mask == (1 << n) - 1:
            return graph[pos][0]
        if dp[pos][mask] is not None:
            return dp[pos][mask]
        min_cost = float('inf')
        for city in range(n):
            if (mask & (1 << city)) == 0:
                cost = graph[pos][city] + tsp(mask | (1 << city), city)
                min_cost = min(min_cost, cost)
        dp[pos][mask] = min_cost
        return min_cost
    return tsp(1, 0)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
tsp_cost = tsp_dynamic_programming(graph)
print("Optimal TSP Cost using Dynamic Programming:", tsp_cost)
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)