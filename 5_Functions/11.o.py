def combinationSum(arr, target):
    result = []
    arr.sort()  # Optional: Sorting helps with optimization
    
    def backtrack(start, path, current_sum):
        if current_sum == target:
            result.append(path.copy())
            return
        if current_sum > target:
            return
        
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i, path, current_sum + arr[i])  # not i+1 because we can reuse the same element
            path.pop()
    
    backtrack(0, [], 0)
    return result

# Example usage:
arr = [2, 4, 6, 8]
target = 8
combinations = combinationSum(arr, target)
for combo in combinations:
    print(combo)
