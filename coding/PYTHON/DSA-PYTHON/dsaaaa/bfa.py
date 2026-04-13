import collections#breath first search
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    def bfs(self, startnode):
        seen, queue = set([startnode]), collections.deque([startnode])
        while queue:
            vertex = queue.popleft()
            self.marked(vertex)
            for node in self.gdict[vertex]:
                if node not in seen:
                    seen.add(node)
                    queue.append(node)
    def marked(self, n):
        print(n)
gdict = {
    "a": set(["b", "c"]),
    "b": set(["a", "d"]),
    "c": set(["a", "d"]),
    "d": set(["e"]),
    "e": set(["a"])
}
graph = Graph(gdict)
graph.bfs("a")