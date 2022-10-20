#Meu primeiro projeto Python!!!


print("Hello, world!")

nome=str(input("Qual é o seu nome? "))
idade=int(input("Quantos anos você tem? "))
print("Olá",nome,"sua idade é:",idade,"anos.")

print("Minha idade é "+str(idade))
print(f"Minha idade é {idade}\n")
print("Minha idade é {}".format(idade))

#Quando quiser usar mais de uma variável usando o .format: 
print("Meu nome é {} e tenho {} anos".format(nome, idade))
