#Funciones de orden superior
from random import randint, uniform,random

def factorial(x):
	if x == 0:
		return 1
	return x*factorial(x-1)

x = input("Factorial de: ")
print(factorial(int(x)))
######################################
print("\n\n\n")
def Digitos(n):
	if n== 0:
		return 0
	return 1+Digitos(int(n/10))
n = input("Digitos de: ")
print(Digitos(int(n)))
print("\n\n\n")
#####################################
def TiempoDeRata():
	X=randint(1,3)
	print("Camino: ",X)
	if X==1:
		return 3+TiempoDeRata()
	if X==2:
		return 5+TiempoDeRata()
	if X==3:
		return 7
print("Tiempo de la rata fue: ",TiempoDeRata())
print("\n\n\n")
###########################################
def PotQuestion(a,b):
	if a==1:
		return True
	if int(a)==0:
		return False
	return PotQuestion(a/b,b)
a = input("Primer numero: ")
b = input("Segundo numero: ")
print(a," es potencia de ",b,"? ")
print(PotQuestion(int(a),int(b)))
print("\n\n\n")
##########################################333
def par(n):
	if n==0:
		return "Es par"
	return impar(n)
def impar(n):
	if n==1:
		return "Es impar"
	return par(n-2)

n=input("Numero a valorar paridad: ")

print(par(int(n)))
print("\n\n\n")
#########################################
def mayor(d):
	if d[0]>d[1]:
		d.remove(d[1])
	else:
		d.remove(d[0])
	if len(d)==1:
		return d
	return mayor(d)
d=input("Lista: ")
print(d)
#d=[1,2,3,4,5,9,6,7,8,0]
print(mayor(list(d)))



