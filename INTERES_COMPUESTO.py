print("--------------------------------------")
print("--------------------------------------")
print("         INTERES COMPUESTO            ")
print("--------------------------------------")
print("--------------------------------------")


c  = int(input("DIGITE EL VALOR DE SU CAPITAl: "))

n = 0.05
mes = 0
D = 2*c


while (c < D ):
    c = n + c
    mes = mes + 1
    print("MES: "+ str(mes))
    print("Capital: "+ str(c))
print("LOS MESES NECESARIOS SON: "+ str(mes))



