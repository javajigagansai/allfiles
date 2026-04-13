class Graph:#depth first search
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start)
        for next in self.gdict[start] - visited:
            self.dfs(next, visited)
        return visited
gdict = {
    "a": set(["b", "c"]),
    "b": set(["a", "d"]),
    "c": set(["a", "d"]),
    "d": set(["e"]),
    "e": set(["a"])
}
graph = Graph(gdict)
graph.dfs('a')
