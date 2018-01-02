from collections import defaultdict

class Graph1:
  
  def __init__(self):
    self.graph = defaultdict(list)
  
  def addEdge(self,v,w):
    self.graph[v].append(w)
  
  def DFSU(self,v,visited):
    visited[v] = True
    print(v)
    
    for i in self.graph[v]:
      if visited[i] == False:
        self.DFSU(i,visited)
        
  def DFS(self,v):
    visited = [False]*(len(self.graph))
    self.DFSU(v,visited)

g = Graph1()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.DFS(2)
