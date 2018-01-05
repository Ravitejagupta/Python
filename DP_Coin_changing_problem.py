def coin_changing(coins,sum):
  no_of_coins = [10000]*(sum+1)
  coin = [-1]*(sum+1)
  no_of_coins[0] = coin[0] = 0
  
  for i in range(len(coins)):
    for j in range(1,sum+1):
      if j>= coins[i]:
        if(min(no_of_coins[j],no_of_coins[j-coins[i]]) != no_of_coins[j]):
          no_of_coins[j] = 1+ min(no_of_coins[j],no_of_coins[j-coins[i]])
          coin[j] = i
  total_coins  = no_of_coins[sum]
  print("no_of_coins = {}".format(total_coins))
  print("coins are ")
  while total_coins !=1:
    c = coins[coin[sum]]
    print(c)
    total_coins = no_of_coins[c]
    sum = sum - c
  print(coins[coin[sum]])

coin_changing([7,2,3,6],13)
