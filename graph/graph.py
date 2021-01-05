from collections import defaultdict


class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None


class GraphL:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, src, dst):
        self.graph[src].append(dst)

    def bfs(self, starting_vertex):
        visited = [False] * self.vertices
        queue = []
        bfs = []
        queue.append(starting_vertex)
        visited[starting_vertex] = True
        while queue:
            s = queue.pop(0)
            bfs.append(s)
            for adj_vertex in self.graph[s]:
                if visited[adj_vertex] is False:
                    queue.append(adj_vertex)
                    visited[adj_vertex] = True

        return bfs

    def dfs(self, starting_vertex):
        visited = [False] * self.vertices
        stack = []
        dfs = []
        stack.append(starting_vertex)
        visited[starting_vertex] = True
        while stack:
            s = stack.pop()
            dfs.append(s)
            for adj_vertex in self.graph[s]:
                if visited[adj_vertex] is False:
                    stack.append(adj_vertex)
                    visited[adj_vertex] = True
        return dfs

    def topological(self):
        top = []
        queue = []
        in_degree = [0] * self.vertices
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1
        for i in range(self.vertices):
            if in_degree[i] == 0:
                queue.append(i)
        cnt = 0
        while queue:
            s = queue.pop(0)
            top.append(s)
            for adj_vertex in self.graph[s]:
                in_degree[adj_vertex] -= 1
                if in_degree[adj_vertex] == 0:
                    queue.append(adj_vertex)
            cnt += 1
        if cnt != self.vertices:
            # loop in graph
            print("topological sort not possible")
        return top


g = GraphL(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 4)

print(g.bfs(2))
print(g.dfs(2))
g = GraphL(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)
print(g.topological())