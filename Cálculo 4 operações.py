def soma  (x,y):
    return x+y

def subtraçao (x,y):
    return x-y

def multi (x,y):
    return x*y

def divisao (x,y):
    if y != 0:
        return x/y
    else:
        return "Erro: Divisão por zero"
    

print("escolha a operação:")
print("1. adição")
print("2.subtração")
print("3. multiplicação")
print("4. divisão")


opcao = input("Digite a operação que deseja realizar:")


numero1 = float(input('DIgite o primero numero:'))
numero2 = float(input('DIgite o segundo numero:'))


if opcao == '1':
    resultado = soma (numero1, numero2)
    print(f"{numero1} + {numero2} = {resultado}")
elif opcao == '2':
    resultado = subtraçao (numero1, numero2)
    print(f"{numero1} - {numero2} = {resultado}")
elif opcao == '3':
    resultado = multi (numero1, numero2)
    print(f"{numero1} * {numero2} = {resultado} ")
elif opcao == '4':
    resultado = divisao (numero1, numero2)
    print(f"{numero1} / {numero2} = {resultado}")
else:
    print("opção invalida. por favor, escolha uma operação valida")
    
