fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count+1
    pos = line.find(':')
    data = line[pos+1:]
    data = data.rstrip()
    total = total+float(data)
    
ans = total/count
print("Average spam confidence:", ans)