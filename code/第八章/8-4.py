def getdp1(arr):
   n = len(arr)
   dp = [0] * n
   for i in range(n):
       dp[i] = 1
       for j in range(i):
           if arr[i] > arr[j]:
               dp[i] = max(dp[i], dp[j] + 1)
   return dp
def generateLIS(arr, dp):
   n = max(dp)
   index = dp.index(n)
   lis = [0] * n
   n -= 1
   lis[n] = arr[index]
   # 从右向左
   for i in range(index, 0 - 1, -1):
       # 关键
       if arr[i] < arr[index] and dp[i] == dp[index] - 1:
           n -= 1
           lis[n] = arr[i]
           index = i
   return lis