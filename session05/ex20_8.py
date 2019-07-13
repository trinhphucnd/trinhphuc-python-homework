data = input("Enters the data ?").lower().replace(" ","")

counts = {}
for c in data:
    counts[c]=counts.get(c,0) +1
for c, n in sorted(counts.items()):
    print(c, n)
