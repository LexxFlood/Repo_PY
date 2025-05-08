salario = float(input("infome qual e o seu salario:"))

if salario<=3000:
    print ("programador base")
elif salario>= 3000 and salario<= 6000:
    print ("programador ok")
elif salario>= 6000 and salario<= 15000:
    print ("programador bom")
else:
    print ("excelente")