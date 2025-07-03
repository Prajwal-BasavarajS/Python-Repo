def count_distinct_subsequences(s):
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Empty subsequence
    
    last_occurrence = {}
    
    for i in range(1, n + 1):
        dp[i] = 2 * dp[i - 1]
        ch = s[i - 1]
        if ch in last_occurrence:
            dp[i] -= dp[last_occurrence[ch] - 1]
        last_occurrence[ch] = i
        
    return dp[n]

def betterString(s1, s2):
    count1 = count_distinct_subsequences(s1)
    count2 = count_distinct_subsequences(s2)
    
    if count1 >= count2:
        return s1
    else:
        return s2

# Example usage:
s1 = input().strip()
s2 = input().strip()
print(betterString(s1, s2))
