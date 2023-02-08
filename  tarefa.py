n1 = float(input("INSIRA NOTA DA PRIMEIRA DICIPLINA"))
n2 = float(input("INSIRA NOTA DA SEGUNDA DICIPLINA"))
n3 = float(input("INSIRA NOTA DA TERCEIRA DICIPLINA"))
me = float(input("QUAL A MEDIA ?"))
ma = (n1 + n2*2 + n3*3 + me)/7


if ma >= 9:
    print ("TU É PICA, CARA")
else:
    print("RECUPERAÇÃO, ANIMAL")
    