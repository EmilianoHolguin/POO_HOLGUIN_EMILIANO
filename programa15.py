edades = [11,15,16,17,18,25,21,30]

mayores_edad=[]
menores_edad=[]

for edad in edades:
    if edad <= 17:
        menores_edad.append(edad)
    else:
        mayores_edad.append(edad)

print("Mayores de edad:", mayores_edad)
print("Menores de edad:", menores_edad)
