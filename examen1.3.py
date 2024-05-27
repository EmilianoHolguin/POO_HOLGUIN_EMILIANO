edades = [10,9,14,18,17,25,21,5,15,28,30,45]

infancia=[]
adolescencia=[]
jovenes=[]
adultos=[]

for edad in edades:
    if edad <= 11:
        infancia.append(edad)
    elif edad <= 17:
        adolescencia.append(edad)
    elif edad <= 26:
        jovenes.append(edad)
    else:
        adultos.append(edad)

print("infancia", infancia)
print("adolescencia", adolescencia)
print("jovenes", jovenes)
print("adultos", adultos)
