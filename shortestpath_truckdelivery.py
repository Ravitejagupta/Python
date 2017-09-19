import math

def closestlocations(totalCrates, allLocations, truckCapacity):
  
  list1 =[]
  for i in allLocations:
    list1.append([math.sqrt(i[0]*i[0] + i[1]*i[1]),i[0],i[1]])
  
  list2 = []
  for i in list1:
    list2.append(i[0])
  list2.sort()
  
  i=0
  res = []
  while(i<truckCapacity):
    for k in list1:
      if list2[i] == k[0]:
        res.append([k[1],k[2]])
        i+=1
  print(res[:truckCapacity])
  return(res[:truckCapacity])
  
closestlocations(3,[[3,6],[2,4],[5,3],[2,7],[1,8],[7,9]],3)
