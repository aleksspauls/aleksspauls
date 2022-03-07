
vards = input("Ievadi tekstu")
vards vards.split
vardi = len(vards.split())
print("vārdu skaits - " vardi)

vards = vards.lower()
rakstzimes=['a','ā','b','c','č','d','e','ē','f','g','ģ','h','i','ī','j','k','ķ','l','ļ','m','n','ņ','o','p','q','r','s','š','t','u','ū','v','w','x','y','z','ž', ',', '.', '?', '!', '-', '(', ')']
for i in range(0,44):
    skaits = vards.count(rakstzimes[i])
    if skaits != 0:
        print("rakstzīmju skaits - " alfabets[i],skaits2)

teikumi = sent_tokenize(vardi)
print("teikumu skaists - " len(vardi))
