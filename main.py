#functions
def sorozateleme(nn):
    return 5*nn - 2

#0
print("sorozat elemeinek meghatározása")

#1
db = int(input("kérem az elemek számát:"))

#2
an = []
for n in range(1, db+1):
    an.append(sorozateleme(n))

#3
tempStr = []
for item in an:
    tempStr.append( str(item) )

kiiras = "; ".join(tempStr)
print(kiiras)



