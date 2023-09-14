#Use 'mbox-short.txt' as the file name...

fh = input ("Enter file name: ")
fname = open(fh)
count = 0
total = 0
average = 0
for line in fname:
 
 if  line.lower().startswith('x-dspam-confidence:'):
    count = count + 1
  
    line_list=line.split(" ")
    confidence = float(line_list[1].rstrip())
    total = confidence + total
average = total / count

print("Count:",count)
print("Total:",total)
print("Average spam confidence:", average)







           







