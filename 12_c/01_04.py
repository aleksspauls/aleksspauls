# Ierakstīšana failos ir tikpat vienkārša kā nolasīšana, tomēr jāņem vērā divas lietas:
# 1. teksta failā var ierakstīt tikai <str> datus vai masīvu ar <str>. Tātad viss pirms tam jāpārveido.
# 2. jānorāda piemērota ierakstīšanas atslēga. a – append, papildina failu. w – write, vienmēr raksta no jauna

# Vienkāršs ieraksta piemērs
def piemers1():
    vards = input("Kā Tevi sauc?")
    vecums = int(input("Cik Tev gadu?"))
    ierakstisanai = vards + " " + str(vecums) + "\n"

    with open("aptauja.txt", "a", encoding='utf-8') as fails:
        fails.write(ierakstisanai)

# Masīva ar str'iem ierakstīšana
def piemers2():
    bakterijas = ["Bacteria\n", "Protozoa\n", "Chromista\n", "Plantae\n", "Fungi\n", "Animalia\n"]
    with open("bakterijas.txt", "w", encoding='utf-8') as fails:
        fails.writelines(bakterijas)

