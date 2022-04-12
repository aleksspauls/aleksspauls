def baltapasaka():
    pasaka = with open("balta-pasaka.txt")
    count.letters(pasaka)
    pasaka = with open("balta-pasaka.txt") as fails:
        fails.writelines(pasaka)
    
