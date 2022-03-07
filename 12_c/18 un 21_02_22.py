import random

īpašība = ['lielais', 'mazais', 'ātrais', 'veiklais', 'gausais']
lieta = ['galds', 'suns', 'traktors' ,'šņore']
darbība = ['tamborē', 'šuj', 'ada', 'skrien']

saraksts1 = random.choise(īpašība)
saraksts2 = random.choise(lieta)
saraksts3 = random.choise(darbība)


rezultats = (saraksts1.capitalize()+saraksts2.capitalize()saraksts3.capitalize())

rezultats = rezultats.replace("a", "@")
rezultats = rezultats.replace("s", "$")
rezultats = rezultats.replace("i", "!")

print(rezultats)
