import os
import time

from services import restaurante_service

nome = input("Digite o nome do restaurante \n")
os.system("cls")

restaurante = restaurante_service.Restaurante(nome)

while True:
    os.system("cls")

    print(f" {nome.title()} ".center(30, "="))
    opcao = int(input("Escolha uma opção:\n" \
    "[1] Registrar venda\n"
    "[2] Visualizar resultados\n"
    "[9] Sair\n"
    "Sua opção: "))
    
    os.system("cls")
    match opcao:
        case 1:
            preco_produto = float(input("Insira o valor do produto\nR$"))
            os.system("cls")

            if restaurante.registrar_venda(preco_produto):
                print(f"Prato registrado no valor de R${preco_produto}")
            else:
                 print("Valor inválido, favor inserir um valor maior que 0")
            time.sleep(2)

        case 2:
            restaurante.resultados()
            input("\nPressione qualquer tecla para continuar\n")
        
        case 9:
            print("Você escolheu sair")
            time.sleep(2)
            break

        case _:
            print("Opção inválida")
            time.sleep(2)