con1={1,2,3,4,5}
con2={6,7,8,9,10}
con3={11,12,13,14,15}

union = con1|con2|con3

#PARA IMPIRMIR SOLAMENTE LOS NUMEROS PARES SE PONE % 2 == 0:
unionpares = { numeros for numeros in union if numeros % 2 == 0}

print("Los numeros pares en el nuevo conjunto son:",unionpares)