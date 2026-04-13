query = "best python tutorials for data science beginners"
words = query.split()
pos_seq = [(w,"N") if len(w)>3 else (w,"O") for w in words]
chunks = []
for i in range(len(pos_seq)-1):
    if pos_seq[i][1]=="N" and pos_seq[i+1][1]=="N":
        chunks.append(pos_seq[i][0]+" "+pos_seq[i+1][0])
print("Keyword phrases:", chunks)