def getdp2(arr):
   n = len(arr)
   dp, ends = [0] * n, [0] * n
   ends[0], dp[0] = arr[0], 1
   right, l, r, m = 0, 0, 0, 0
   for i in range(1, n):
       l = 0
       r = right
       # 二分查找,若找不到则ends[l或r]是比arr[i]大而又最接近其的数
       # 若arr[i]比ends有效区的值都大，则l=right+1
       while l <= r:
           m = (l + r) / 2
           if arr[i] > ends[m]:
               l = m + 1
           else:
               r = m - 1
       right = max(right, l)
       ends[l] = arr[i]
       dp[i] = l + 1
   return dp