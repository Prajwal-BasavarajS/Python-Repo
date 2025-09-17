d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15}

# Extract keys as a list
# myKeys = list(d.keys())   # ['ravi', 'rajnish', 'sanjeev']

# Sort keys alphabetically
# myKeys.sort()             # ['rajnish', 'ravi', 'sanjeev']

# Build new dictionary in sorted order
# sd = {i: d[i] for i in myKeys}

sd = dict(sorted(d.items(), key=lambda item: item[1]))
print(sd)
