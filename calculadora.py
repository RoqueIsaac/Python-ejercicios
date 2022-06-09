# -*- coding: utf-8 -*-

def ndef():
    print("Opcion no valida !!")
    return

def case(r,a,b):
    switcher = {
       1: suma,
       2: resta,
       3: mult,
       4: div,
       5: modulo,
       6: potencia
    }
    operacion=switcher.get(r,ndef)
    operacion(a,b)

def nums():
    a=float(input("Numero a: "))
    b=float(input("Numero b: "))
    return a,b

def suma(a,b):
    print("%.2f + %.2f = %.2f" % (a,b,a+b))
    return
    
def resta(a,b):
    print ("%.2f - %.2f = %.2f" % (a,b,a-b))
    return

def mult(a,b):
    print ("%.2f * %.2f = %.2f" % (a,b,a*b))
    return

def div(a,b):
    if (b==0):
        print ("Div 0 no valido")
    else:
        print ("%d / %d = %.2f" % (a,b,a / b))
    return

def modulo(a,b):
    if (b==0):
        print ("Mod 0 no valido")
    else:
        print ( str(a) + " % " + str(b) + " = " + str(a%b))
    return

def potencia(a,b):
    print("%.2f ^ %.2f = %.2f" % (a,b,pow(a,b)))

#-------------------------------------------------

k=0
while(k!=3):
    print("")
    print(("Calculadora").center(30,'-'))
    print("Dame una opcion....")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicacion")
    print("4.- Division")
    print("5.- Modulo")
    print("6.- Potencia")
    print(" ")
    print("7.- Salir")
    
    p=int(input("Opcion: "))
    p=int(p)
    
    if (p in [1,2,3,4,5,6]):
        a,b=nums()
        case(p,a,b)
        k=0
        print("\n")
    elif (p==7):
        break
    else:
        ndef()
        k=k+1