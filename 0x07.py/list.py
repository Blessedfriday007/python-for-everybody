# use romeo.txt as the file name...
fname = input ("Enter file name: ")
fh = open (fname)
words = []
for line in fh:
    for word in line.split():
        if word not in words:
            words.append(word)

# Sort the list of unique words and print them
words.sort()
print(words)

    

