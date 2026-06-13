#User function Template for python3
count = 0


class Solution:
    def cutRod(self, price):
        #code here
        
        global count
        n = len(price)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # skipping the cuts that have already been optimized over the original prices
            if dp[i] > price[i-1]: continue
            
            for j in range(i, n + 1):
                dp[j] = max(dp[j], price[i-1] + dp[j-i])
                count += 1
    
        return max(dp)

Solution().cutRod([1,5,8,9,10,17,17,20])

print(count)