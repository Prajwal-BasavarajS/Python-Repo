s = "hello world"

# Split `s` into words
w = s.split()

# process each word in the list `w`
res = ' '.join([
  
    # If the word has more than 1 character
    i[0].upper() + i[1:-1] + i[-1].upper() 
    if len(i) > 1 else i.upper()  # If word has only 1 char, capitalize the whole word
    for i in w  # Iterate through each word in the list `w`
])
print(res)




s = "welcome to geeksforgeeks"
res = ' '.join(
    map(
        lambda word: word[0].upper() + word[1:-1] + word[-1].upper()  # Capitalize first and last character
        if len(word) > 1 else word.upper(),  # If word length is 1, capitalize the whole word
        s.split()  # Split `s`into words
    )
)
print(res)
