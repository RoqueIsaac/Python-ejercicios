# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 00:15:14 2022

@author: Roque Isaac
"""

from random import randrange
from random import randint


def DisplayBoard(x):
    # la función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola
    #
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(x[0][0], x[0][1], x[0][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(x[1][0], x[1][1], x[1][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(x[2][0], x[2][1], x[2][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    
    
def EnterMove(x):
    #
    # la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario
    #
    global used
    while(1):
        p=input("selecciona 1 numero del 1-9: ")
        print("")
        if p not in ["1","2","3","4","5","6","7","8","9"]:
            print("opcion no valida\n")
            continue
        else:
            p=int(p)
            if p not in used:
                used.append(p)
                div=p/3.0
                q=p%3
                if div<=1:
                    x[0][q-1]="O"  #cuando q=0, al ser q-1=-1, pone O al ultimo elemento
                elif div>1 and div<=2:
                    x[1][q-1]="O"
                elif div>2 and div<=3:
                    x[2][q-1]="O"
                break
            else:
                print("numero ocupado, selecciona otro")
    

def MakeListOfFreeFields(x):
    #
    # la función examina el tablero y construye una lista de todos los cuadros vacíos 
    # la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
    #
    q=list()
    ff=tuple()
    c1=0
    
    for j in x:
        c2=0
        for k in j:
            if k not in ["X","O"]:
                tpm=(str(c1)+str(c2))
                ff=tpm,
                q.append(ff)
            c2+=1
        c1+=1
    #print(q)
    if len(q)==0:
        return 0
    else:
        return 1
    
def VictoryFor(x):
    #global sign
    #
    # la función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego
    #
    
    
    if ((x[0][0] == x[0][1] == x[0][2]) or\
       (x[1][0] == x[1][1] == x[1][2]) or\
       (x[2][0] == x[2][1] == x[2][2]) or\
       (x[0][0] == x[1][0] == x[2][0]) or\
       (x[0][1] == x[1][1] == x[2][1]) or\
       (x[0][2] == x[1][2] == x[2][2]) or\
       (x[0][0] == x[1][1] == x[2][2]) or\
       (x[0][2] == x[1][1] == x[2][0])):
        #sign=1
        return 1
    else:
        return 0
       

def DrawMove(x):
    #
    # la función dibuja el movimiento de la maquina y actualiza el tablero
    #
    global used,count
    print("CPU")
    if count:   #primer movimiento
        x[1][1]="X"
        count=0
    else:
        while(1):
            p=randint(1,9)
            if p not in used:
                print(p)
                used.append(p)
                div=p/3.0
                q=p%3
                if div<=1:
                    x[0][q-1]="X"
                elif div>1 and div<=2:
                    x[1][q-1]="X"
                elif div>2 and div<=3:
                    x[2][q-1]="X"
                break
            
#------------------------------------

k='s'
while(k=='s'):
    #[["-" for j in range(1,4)] for k in range(1,4)]    
    x=[[1,2,3],[4,5,6],[7,8,9]]
    count=1 #indica primer mov, de CPU
    sign=0  #indica ganador
    used=[5]  #numeros ya utilizados, primero el pc al centro
    DisplayBoard(x)
    print("CPU primero")
    DrawMove(x)
    DisplayBoard(x)
    while(sign==0):
        EnterMove(x)
        DisplayBoard(x)
        if (VictoryFor(x)):
            print("Ganaste")
            break
        #if(MakeListOfFreeFields(x)==0):
            #    print("no mas espacio")
            #    break
        DrawMove(x)
        DisplayBoard(x)
        if (VictoryFor(x)):
            print("CPU is the winner")
            break
        if(MakeListOfFreeFields(x)==0):
            print("no mas espacio")
            break
    print("\n")

    while(True):
        k=str(input("quieres jugar de nuevo (s/n) ? "))
        if k not in ['n','N','s','S']:
            print("opcion invalida")
            print("\n")
        else:
            break
            
    

print("Se ha acabado")