
# idade = int(input("Digite a sua idade: "))


# if idade < 12:
#     print("Criança")
# elif 12 <= idade <= 17:
#     print("Adolescente")
# elif 18 <= idade <= 59:
#     print("Adulto")
# else:
#     print("Idoso")



# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# num3 = float(input("Digite o terceiro número: "))


# maior = max(num1, num2, num3)


# menor = min(num1, num2, num3)


# print(f"O maior número é: {maior}")
# print(f"O menor número é: {menor}")

# quantidade_pares = 0
# quantidade_impares = 0

# quantidade_pares = 0 
# for i in range(10):
#     numero = int(input(f"digite o {i+1} numero: "))

#     if numero % 2 == 0:
#         quantidade_pares +=1
#     else:
#         quantidade_impares += 1 

# print(f"quantidade de numeros pares: {quantidade_pares}")
# print(f"quantidade de numeros impares: {quantidade+impares}")



# n = int(input("Digite o número de pessoas: "))
# soma_idades = 0

# for i in range(n):
#     idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
#     soma_idades += idade

# media_idade = soma_idades / n

# if media_idade <= 25:
#     print("A turma é jovem.")
# elif 26 <= media_idade <= 60:
#     print("A turma é adulta.")
# else:
#     print("A turma é idosa.")


# print(f"A média de idade da turma é: {media_idade:.2f}")



# n = int(input("Digite o número de elementos: "))

# menor = float('inf')  
# maior = float('-inf')  
# soma = 0


# for i in range(n):
#     numero = float(input(f"Digite o {i+1}º número: "))
    
#     soma += numero
    

#     if numero < menor:
#         menor = numero
    

#     if numero > maior:
#         maior = numero

# print(f"O menor valor é: {menor}")
# print(f"O maior valor é: {maior}")
# print(f"A soma dos valores é: {soma}")



total_gasto = 0
produtos_mais_1000 = 0
produto_mais_barato = ""
preco_mais_barato = float('inf')  


while True:
    
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: R$ "))

    total_gasto += preco_produto

    if preco_produto > 1000:
        produtos_mais_1000 += 1

    if preco_produto < preco_mais_barato:
        preco_mais_barato = preco_produto
        produto_mais_barato = nome_produto
    

    continuar = input("Deseja adicionar mais produtos? (s/n): ").strip().lower()
    if continuar != 's':
    break


print("\nResumo da compra:")
print(f"Total gasto: R$ {total_gasto:.2f}")
print(f"Quantidade de produtos acima de R$1000: {produtos_mais_1000}")
print(f"Produto mais barato: {produto_mais_barato} (R$ {preco_mais_barato:.2f})")
