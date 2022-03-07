# Izveido programmu, kurā var ievadīt tekstu un programma parāda katra burta skaitu tajā (lielos un mazos var skaitīt kopā). Izmatojiet ciklu!

vards = input("Ievadi teikumu")
vards = vards.lower()
alfabets=['a','ā','b','c','č','d','e','ē','f','g','ģ','h','i','ī','j','k','ķ','l','ļ','m','n','ņ','o','p','q','r','s','š','t','u','ū','v','w','x','y','z','ž']
for i in range(0,37):
    skaits = vards.count(alfabets[i])
    if skaits != 0:
        print(alfabets[i],skaits)
