burtiSTR = "qwertyuiopasdfghjklzxcvbnmēŗūīōāšģķļžčņ"
burti = list(burtiSTR)
burti.sort()
cipariSTR = "1234567890"
zimesSTR = ",.?!:;'"
cipari = list(cipariSTR)
zimes = list(zimesSTR)
rakstzimes = burti + cipari + zimes


def skaita():
    with open("balta-pasaka.txt", "r") as fails:
        teksts = fails.read()
    
    teksts = teksts.lower()

    for viena in rakstzimes:
        cik = teksts.count(viena)
        if cik > 0:
            print(f"{viena}: {cik}")

skaita()
