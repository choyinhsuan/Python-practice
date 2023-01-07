fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    tmp = line.split()
    for word in tmp:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
