from Levenshtein import distance as lev
exec(open("./swadesh.py").read())

totdist = 0
iter = 0
for i,k in zip(miipa, coipa):
        dist = lev(i, k)
        #print("Distanza "+i+ "-" + k + " pari a: " + str(dist))
        totdist = totdist + dist
        iter = iter + 1
print("Distanza media tra Milanese e Comasco: ")
print(totdist/iter)
print(str(totdist) + "/" +str(iter))

totdist = 0
iter = 0
for i,k in zip(miclas, minol):
        dist = lev(i, k)
        #print("Distanza "+i+ "-" + k + " pari a: " + str(dist))
        totdist = totdist + dist
        iter = iter + 1
print("Distanza media tra MILCLASS e NOL-MI: ")
print(totdist/iter)
print(str(totdist) + "/" +str(iter))

totdist = 0
iter = 0
for i,k in zip(conol, colsi):
        dist = lev(i, k)
        #print("Distanza "+i+ "-" + k + " pari a: " + str(dist))
        totdist = totdist + dist
        iter = iter + 1
print("Distanza media tra NOL-CO e LSI-CO: ")
print(totdist/iter)
print(str(totdist) + "/" +str(iter))


totdist = 0
iter = 0
for i,k in zip(miclas, colsi):
	dist = lev(i, k)
	#print("Distanza "+i+ "-" + k + " pari a: " + str(dist))
	totdist = totdist + dist
	iter = iter + 1
print("Distanza media tra MILCLASS e LSI-CO: ")
print(totdist/iter)
print(str(totdist) + "/" +str(iter))

totdist = 0
iter = 0
for i,k in zip(minol, conol):
        dist = lev(i, k)
        #print("Distanza "+i+ "-" + k + " pari a: " + str(dist))
        totdist = totdist + dist
        iter = iter + 1
print("Distanza media tra CO-NOL e MI-NOL: ")
print(totdist/iter)
print(str(totdist) + "/" +str(iter))

totdist = 0
iter = 0
for i,k in zip(ptipa, coipa):
        dist = lev(i, k)
        #print("Distanza "+i+ "-" + k + " pari a: " + str(dist))
        totdist = totdist + dist
        iter = iter + 1
print("Distanza media tra Portoghese e Comasco: ")
print(totdist/iter)
print(str(totdist) + "/" +str(iter))

totdist = 0
iter = 0
for i,k in zip(ptipa, itipa):
        dist = lev(i, k)
        #print("Distanza "+i+ "-" + k + " pari a: " + str(dist))
        totdist = totdist + dist
        iter = iter + 1
print("Distanza media tra Portoghese e Italiano: ")
print(totdist/iter)
print(str(totdist) + "/" +str(iter))

totdist = 0
iter = 0
for i,k in zip(coipa, itipa):
        dist = lev(i, k)
        #print("Distanza "+i+ "-" + k + " pari a: " + str(dist))
        totdist = totdist + dist
        iter = iter + 1
print("Distanza media tra Comasco e Italiano: ")
print(totdist/iter)
print(str(totdist) + "/" +str(iter))

totdist = 0
iter = 0
for i,k in zip(miipa, itipa):
        dist = lev(i, k)
        #print("Distanza "+i+ "-" + k + " pari a: " + str(dist))
        totdist = totdist + dist
        iter = iter + 1
print("Distanza media tra Milanese e Italiano: ")
print(totdist/iter)
print(str(totdist) + "/" +str(iter))

totdist = 0
iter = 0
for i,k in zip(miipa, ptipa):
        dist = lev(i, k)
        #print("Distanza "+i+ "-" + k + " pari a: " + str(dist))
        totdist = totdist + dist
        iter = iter + 1
print("Distanza media tra Milanese e Portoghese: ")
print(totdist/iter)
print(str(totdist) + "/" +str(iter))
