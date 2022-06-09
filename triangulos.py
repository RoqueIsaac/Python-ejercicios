# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 17:49:21 2021

@author: Roque Isaac
"""

print("Triangulo derecho")
n=10
if (n%2==0):
    n=n+1
k=0
for i in range(n):
    if ( i <= (n/2)):
        k=k+1
        for j in range(k):
            print("*",end='')
    if(i>(n/2)):
        k=k-1
        for j in range(k):
            print("*",end='')
    print(" ")
    
"""-----------------"""
print(" ")
print("Triangulo izquierdo")

k=0
n=10
if (n%2==0):
    n=n+1
    
for i in range(n):
    if (i <= (n/2)):
        for j in range (int(n/2) -k +30):
            print(" ",end='')
        for j in range (k+1):
            print("*",end='')
        k=k+1
    if  (i > (n/2)):
        k=k-1
        for j in range(int(n/2) - k + 1 +30):
            print(" ",end='')
        for j in range(k):
            print("*",end='')
    print(" ")
    

"""-----------------"""

print(" ")
print(("Doble Triangulo").center(30,'-'))

k=0
n=10
if (n%2==0):
    n=n+1

for i in range(n):
    if (i <= (n/2)):
        k=k+1
        for j in range(k):
            print("*",end='')
        #espejo
        for j in range(int(n/2) -2*k + 30):
            print(" ",end='')
        for j in range(k):
            print ("*",end='')
    if (i > (n/2)):
        k=k-1
        for j in range(k):
            print("*", end='')
        #espejo
        for j in range(int(n/2) -2*k +30):
            print(" ",end='')
        for j in range (k):
            print("*",end='')
    print(" ")


"""-----------------"""

print(" ")
print(("Doble Triangulo 2").center(30,'-'))
print(" ")

k=0
n=10
if (n%2==0):
    n=n+1

for i in range(n):
    if ( i <= (n/2)):
        for j in range(int(n/2)-k):
            print(" ",end='')
        for j in range(k+1):
            print("*",end='')
        k=k+1
        #espejo desplazado
        print(" ",end='')
        for j in range(k):
            print("*",end='')
    if (i > (n/2)):
        k=k-1
        for j in range(int(n/2)-k+1):
            print(" ",end='')
        for j in range(k):
            print("*",end='')
        #espejo desplazado
        print(" ",end='')
        for j in range(k):
            print("*",end='')
        
    print(" ")
print(" ")
            
"""-----------------"""

print(" ")
print(("Rombo").center(30,'-'))
print(" ")

k=0
n=15
if (n%2==0):
    n=n+1

for i in range(n):
    if (i <= (n/2)):
        for j in range(int(n/2)-k+2):
            print(" ",end='')
        for j in range(2*k+1):
            print("*",end='')
        k=k+1
    if (i > (n/2)):
        k=k-1
        for j in range(int(n/2)-k+2+1):
            print(" ",end='')
        for j in range (2*k-1):
            print("*",end='')
    print(" ")
print(" ")
    
"""-----------------"""

print(" ")
print(("Triangulo sup").center(30,'-'))
print(" ")

k=0
n=10
if (n%2==0):
    n=n+1

for i in range(n):
    if(i <= (n/2)):
        for j in range(int(n/2)-k+2):
            print(" ",end='')
        for j in range(2*k+1):
            print("*",end='')
        k=k+1
        print(" ")
print(" ")


"""-----------------"""

print(" ")
print(("Triangulo inf").center(30,'-'))
print(" ")

k=0
n=10
if (n%2==0):
    n=n+1

for i in range(n):
    if (i <= (n/2)):
        for i in range(k+2):
            print(" ",end='')
        for i in range(n-2*k):
            print("*",end='')
        k=k+1
        print("")



