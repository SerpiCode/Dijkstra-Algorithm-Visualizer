import heapq

class Graph:
    def __init__(self, V: int):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def addEdge(self, u: int, v: int, w: int):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    def Dijkstra(self, src: int):
        priority_queue = []
        heapq.heappush(priority_queue, (0, src))

        dist = [float('inf')] * self.V
        dist[src] = 0

        prev = {v: None for v in range(self.V)}
        prev[src] = src

        while priority_queue:
            d, u = heapq.heappop(priority_queue)

            for v, weight in self.adj[u]:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    prev[v] = u
                    heapq.heappush(priority_queue, (dist[v], v))

        # Construct the edges of the resulting graph
        edges = []
        for v in range(self.V):
            if prev[v] is not None and v != src:
                u = prev[v]
                weight = None
                for neighbor, w in self.adj[u]:
                    if neighbor == v:
                        weight = w
                        break
                edges.append((u, v, weight))

        return edges