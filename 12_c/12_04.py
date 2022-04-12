def kartotajs():
    with open("sakarto.txt", "r", encoding="utf-8") as fails:
        dati = fails.readlines()

        vardi = []
        skaitļi = []

    for i in range(len(dati)):
        dati[i] = dati[i].rstrip()
        if dati[i].isdecimal():
            skaitļi.append(dati[i])
        else:
            vardi.append(dati[i])

    vardi.sort()
    skaitļi.sort()

    print(vardi)
    print(skaitļi)
