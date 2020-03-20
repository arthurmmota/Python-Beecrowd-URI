import random
#import ditc.py
from builtins import print


def sayHello():
	return "Ola"
def call_numbers():
	for i in range(0,10):
		print(i * random.randint(1,101))


A = 1000
B = 100
if(A + B) <  200:
	print (sayHello())
elif B < 500:
	print("$$$$")
else:
	print("menor")

'''list.
numeros = [int(input("Número: ")) for i in range(20)]
numeros = []
for i in range(20):
    numeros.append(int(input("Número: ")))'''

lista = []
'''numeros = [int(input("Número: ")) for i in range(20)]'''

for item in range(2):
	lista.append(1+1)

for item in lista:
	print(item)

number = 5
while number < 10:
	print(number)
	number+=1
	#if number == 8:
	#	break
else:
	print("eita", number)

call_numbers()

def cal(x = 8000,y  =85):
	return (x - y)
a = cal(y =555, x=10)

print("Result is" ,a)

#dicinarios

'''arrays asscoaitivos do php '''

people = dict(O = "PAI", E ="MAE", C ="IRMA")
print(people)
if 'O' in people:
	print(people['O'])

