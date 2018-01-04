def subset_sum(a,sum):
  matrix = [[0 for i in range(sum+1)] for i in a]
  for i in range(len(a)):
    for j in range(sum+1):
      if i == 0:
        if j ==0:
          matrix[i][j] = 1
        if a[i] == j:
          matrix[i][j] = 1
      else:
        if j == 0:
          matrix[i][j] = 1
        elif j < a[i]:
          matrix[i][j] = matrix[i-1][j]
        elif(j>=a[i]):
          if matrix[i-1][j] == 1:
            matrix[i][j] = 1
          else:
            matrix[i][j] = matrix[i-1][j-a[i]]
  return(matrix[len(a)-1][sum] == 1)
  
subset_sum([2,3,7,8,10],11)
