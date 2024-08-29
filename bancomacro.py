"""banco macro"""

saldo=float(input("ingrese el saldo actual"))
cod=int(input("ingrese la opcion para operar"))
if cod==1:
 monto=int(input"ingrese el monto a extraer")
 if monto<=saldo:
    print("Puede realizarlo")
    SaldoRes = saldo - monto
    print("Tu saldo actual es: ", SaldoRes)
 else:
    ("No es posible, saldo insuficiente")
 elif cod == 2
 SaldoRes=saldo+50000
 print("Tu saldo actual es: ", SaldoRes)
elif cod==3
 serv=int(input("ingrese el monto del servicio a pagar"))
 if serv<=saldo:
     print("Si puede pagar")
     SaldoRes=saldo-serv
     print("El saldo actual es:", SaldoRes)
 else
 print("El saldo es insuficiente")
 
    


