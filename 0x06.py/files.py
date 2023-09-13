# Use the file name mbox-short.txt as the file name.
fhand = open('mbox-short.txt')
print(fhand)

for line in fhand:
    ly = line.rstrip()
    print (ly.upper())
    
