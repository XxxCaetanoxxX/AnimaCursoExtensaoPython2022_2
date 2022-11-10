print ("Início da aula 3 (09/11/2022)")

contadorFor=0
contadorWhile=0

print("Contagem com Loop for: ")
for i in range(11):
  print(contadorFor)
  contadorFor+=1

print("\n")
print("Loop com o While:")
while contadorWhile <11:
  print(contadorWhile)
  contadorWhile+=1

frutas= ["morango","laranja","pêra"]
print(frutas[0])

print(len(frutas))

frutas.append("manga")
print(len(frutas))
print(frutas)

for i in frutas:
  print(i)

x=0
while x<len(frutas):
  print(frutas[x])
  x+=x

for fruta in frutas:
  print(fruta)


