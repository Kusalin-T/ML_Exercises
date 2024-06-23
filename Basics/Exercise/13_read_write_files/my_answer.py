from itertools import groupby

poemfile = open("C:\\Users\\Buta\\dev\\py\\Basics\\Exercise\\13_read_write_files\\poem.txt", 'r')
txt = poemfile.read().split()
d={}
for w in txt:
    d[w] = d.get(w,0) + 1
maxword=max(d, key=lambda x:d[x])
print(f"Max word is '{maxword}' with {d[maxword]} occurences")
poemfile.close()

with open("C:\\Users\\Buta\\dev\\py\\Basics\\Exercise\\13_read_write_files\\stocks.csv",'r') as f, open("C:\\Users\\Buta\\dev\\py\\Basics\\Exercise\\13_read_write_files\\output.csv",'w') as out:
    out.write('Company Name,PE Ratio,PB Ratio\n')
    next(f)
    for line in f:
        tokens = line.strip('\n').split(',')
        pe = float(tokens[1])/float(tokens[2])
        pb = float(tokens[1])/float(tokens[3])
        out.write(f"{tokens[0]},{pe:.2f},{pb:.2f}\n")   

