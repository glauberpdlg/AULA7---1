
def mostrar_tabuada(numero):
    for i in range(0, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


operacao = int(input("Digite o número para saber a multiplicação: "))
mostrar_tabuada(operacao)

    
