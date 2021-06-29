fname=input("Enter the filename : " )
try:
    fhand=open(fname)
    d1=dict()
    for line in fhand:
        words=line.split()
        for word in words:
            d1[word]=d1.get(word,0) + 1
    print(d1)
except:
    print("File not found ")
