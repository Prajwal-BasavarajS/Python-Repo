def subsetSums(arr):
    result = []
    
    def backtrack(index, current_sum):
        if index == len(arr):
            result.append(current_sum)
            return
        # Include current element
        backtrack(index + 1, current_sum + arr[index])
        # Exclude current element
        backtrack(index + 1, current_sum)
    
    backtrack(0, 0)
    return result

# Example usage:
arr = [2, 3]
print(subsetSums(arr))
