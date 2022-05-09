def uzd1():
    masivs = ["funkcija", "programma", "versija", "interpretators"]
    vardi = masivs.sort

    with open("jedzieni.txt", "a", encoding='utf-8') as fails:
        fails.write("Jedzieni:" + vardi)
