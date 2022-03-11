#kāpņu telpas koda ģenerātors

kods = int(input("Ievadi dzīvokļa numuru"))
viens = ['A', 'B', 'C' ,'D']
divi = ['#', '*']
tris = random.randrange(999, 9999)

saraksts1 = random.choise(viens)
saraksts2 = random.choise(divi)
parole = (kods +saraksts1()+saraksts2()+tris)

if kods(0, 999):
    print(parole)
else:
    print("Nederīgs dzīvokļa numurs")
