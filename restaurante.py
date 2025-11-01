import os
import time

from services import restaurante_service

def limpar_tela():
    os.system("cls")

nome = input("Digite o nome do restaurante \n")
restaurante = restaurante_service.Restaurante(nome)
limpar_tela()


while True:
    limpar_tela()

    print(f" {nome.title()} ".center(30, "="))

    opcao = int(input("Escolha uma opção:\n" \
    "[1] Registrar venda\n"
    "[2] Visualizar resultados\n"
    "[9] Sair\n"
    "Sua opção: "))
    
    limpar_tela()
    match opcao:
        case 1:
            preco_produto = float(input("Insira o valor do produto\nR$"))
            limpar_tela()

            sucess, msg = restaurante.registrar_venda(preco_produto)
            print(msg)
            
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