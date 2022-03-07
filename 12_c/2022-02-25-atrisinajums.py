def analize(teksts):
    vardi = teksts.count(" ") + 1
    rakstzimes = len(teksts) - teksts.count(" ")
    teikumi = teksts.count(".") + teksts.count("?") + teksts.count("!")
    rindkopas = teksts.count("\n") + 1
    print(f"Tekstā ir {vardi} vārdi, {rakstzimes} zīmes, {teikumi} teikumi, {rindkopas} rindkopas")

def tagi(teksts, tags):
    virkne = "<" + tags + ">" + teksts + "</" + tags + ">"
    print(virkne)

analize("Šodien ir saulaina diena. Priekšā divas brīvdienas. Ko lai dara? Zinu!")
tagi("skola", "h1")
