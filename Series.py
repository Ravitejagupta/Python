def series(a):
  if (a%2 ==1):
    print(int(a/2),int(a/2+1))
    return
  for i in range(3,int((2*a)**0.5)+1):
    k = (a - (i*(i+1)/2))/i
    if k - int(k) == 0:
      break;
  for j in range(1,i+1):
    print( (a - i*(i+1)/2)/i + j)

series(123)
