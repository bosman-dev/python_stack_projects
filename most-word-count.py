# Get the name of the file and open it
fname = input('Enter file:')
try:
    fhandle = open(fname, 'r')

except:
    print('File cannot be opened:', fname)
    quit()

# Count word frequency
counts = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

# Find the most common word
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
# All done
print(bigword, bigcount)






