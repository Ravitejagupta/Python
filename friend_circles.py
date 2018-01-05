def findCircleNum(self, M):
      seen = set()
      r = 0
      def dfs(node):
          for j in range(len(M[node])):
              if M[node][j] == 1 and node !=j:
                  if j not in seen:
                      seen.add(j)
                      dfs(j)
      for i in range(len(M)):
          if i not in seen:
              r+=1
              seen.add(i)
              dfs(i)
      return(r)
