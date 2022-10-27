import random


#Loop aleatório de uma lista mostrando apenas um valor dela
linguagens = ['JavaScript', 'Python', 'C#', 'Java', 'PHP']
print(random.choice(linguagens))


#Loop em uma lista mostrando todos os valores dela ordenadamente
frutas = ['Uva', 'Melancia', 'Morango', 'Maracujá', 'Limão']
for f in frutas:
	print(f)


#Loop em uma lista com range de 10 números (0 até 9), mostrando de modo aleatório apenas 3 números dela
numeros = list(range(10))
n = random.sample(numeros, 3)
for num in n:
	print(num)