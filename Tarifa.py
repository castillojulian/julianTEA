def calculoSalario(horas,tarifa):
 horasextras = horas - maxhora_semanal
 if(horasextras>0):
    pago = (maxhora_semanal * tarifa) + (horasextras * (tarifa * 1.5))
 else:
    pago = horas * tarifa
 return pago

maxhora_semanal = 40
horas = int (input("Ingrese la cantidad de horas: "))
tarifa = float(input("Ingrese la tarifa por hora: "))
salario = calculoSalario(horas, tarifa)
print(salario)