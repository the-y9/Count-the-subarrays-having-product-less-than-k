def countSubArrayProductLessThanK( a, n, k):
        count = 0
        prod = 1
        left = 0
        for right in range(n):
            prod *= a[right]
            while prod >= k and left <= right:
                prod //= a[left]
                left += 1
            count += right - left + 1
        return count        
