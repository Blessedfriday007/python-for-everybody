# use romeo.txt as the file name...
words = []
fname = input ("Enter file name: ")
fh = open (fname)


for line in fh:
            # Split the line into words
            line_words = line.split()
            
            # Check each word and append it to the list if it's not already there
            for word in line_words:
                if word not in words:
                    words.append(word)
            words.sort()
        
        # Print the sorted words
            for word in words:
             print(word)

    

