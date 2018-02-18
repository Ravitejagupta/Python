a = [1,4,5,3,6,8,9,2,3,5,10,12]
min1 = sys.maxint
min2 = sys.maxint

for i in a:  
  if i< min1:
    min2 = min1
    min1 = i
  elif(i<min2 and i != min1):
    min2 =i
print(min1,min2)
