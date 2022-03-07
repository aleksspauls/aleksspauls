#tagi("skola", "h1")

def tagi(teksts, tags):
    virkne = "<" + tags + ">" + teksts + "</" + tags + ">"
    print(virkne)

#otrā puse #tagiem



virkne = input("Ievadi pāra skaita simbolu virkni ")
garums = len(virkne)
puse = garums //2
print(virkne[0:puse])
