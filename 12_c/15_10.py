#1

pauguri = ["Gaiziņkalns", "Sirdskalns", "Lielais Liepukalns", "Abrienas kalns", "Dzierkaļu kalns", "Nesaules kalns", "Čiekurkalns"]
print(pauguri[3:6])

#2

pauguri.append("Mazais Gaiziņkalns")
pauguri.extend(["Ķelēnu kalns", "Dravēnu kalns", "Bolēnu kalns"])
pauguri.remove("Čiekurkalns")

print(pauguri.index("Sirdskalns"))


#6
augstumi = [311.94, 296.8, 289.3, 287.4, 286.3, 284.2, 283.6, 283.4, 282.7, 282.5]

#7

##for i in augstumi:
##   print(i)
##
##for x in pauguri:
##    for c in augstumi:
##        print(x,c)

skaits = len(augstumi)
for i in range(skaits):
    print(pauguri[i], augstumi[i])
