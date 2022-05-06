def u1():
    a = input("Ievadi savu vārdu")
    b = input("Ievadi savu uzvārdu")
    c =  a + b + ";"
    print(c) in ("DB.txt")
    

def u2():
    with open("The_Zen_of_Python.txt",'r') as f:
        a = f.readlines()
        b = upper(a)
        print (b)
