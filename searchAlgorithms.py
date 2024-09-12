import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import heapq
from generateGraph import generate,visualize_graph


class TraversalAlgorithms : 
    def dfs_helper(self,i,graph,vis,parent,goal,n):
        if i == goal :
            return
        vis[i] = 1
        for j in range(n):
            if graph[i][j] and not vis[j] :
                parent[j] = i 
                self.dfs_helper(j,graph,vis,parent,goal,n)
        return
    def dfs(self,graph,st,goal):
        vis = [0 for i in range(len(graph))]
        parent = {}
        self.dfs_helper(st,graph,vis,parent,goal,len(graph))
        return parent 
    def bfs_helper(self,i,graph,vis,goal,n):
        queue = []
        queue.append([i,[]])
        while len(queue) :
            # print(queue)
            temp = queue.pop(0)
            current,path = temp[0], temp[1]
            new_path = path + [current]
            if current == goal:
                return new_path
            
            vis[current] = 1
            for j in range(n):
                if not vis[j] and graph[current][j] :
                    queue.append([j,new_path])
        return path
    def bfs(self,graph,st,goal):
        vis = [0 for i in range(len(graph))]
        path = self.bfs_helper(st,graph,vis,goal,len(graph))
        return path
    def ucs_helper(self, i,graph,vis,goal,n):
        min_heap = []
        heapq.heappush(min_heap,[i,0,[]])
        while len(min_heap):
            temp = heapq.heappop(min_heap)
            current,cost,path = temp[0],temp[1],temp[2]
            vis[current] = 1
            new_path = path + [current]
            if current == goal:
                return cost,new_path
            for j in range(n):
                if not vis[j] and graph[current][j]:
                    new_cost = cost + graph[current][j]
                    heapq.heappush(min_heap,[j,new_cost,new_path])
        return 0,[-1]

    def ucs(self,graph,st,goal):
        vis = [0 for i in range(len(graph))]
        path = self.ucs_helper(st,graph,vis,goal,len(graph))
        return path
    def print_path(self,parent,st,goal):
        path = []
        current = goal

        while current in parent:
            path.append(current)
            current = parent[current]
        path.append(st)
        path.reverse()
        print("Path:", path)


if __name__ == "__main__":

    graph = generate(100)
    visualize_graph(graph)
    # DFS Test 
    dfs = TraversalAlgorithms()
    # dfs.visualize_graph(graph)
    dfs.print_path(dfs.dfs(graph,0,6),0,6)
    
    # BFS Test 
    bfs = TraversalAlgorithms()
    # bfs.visualize_graph(graph)
    print(bfs.bfs(graph,0,6))

    ucs = TraversalAlgorithms()
    print(ucs.ucs(graph,0,8))

            
            



    

    

