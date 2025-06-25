# Input dictionary and query list
data = {1: "abc", 2: "cde", 3: "fgh"}
queries = [2, 3, 4]

# Loop through each query and print the result
for key in queries:
    print(data.get(key, "None"))
