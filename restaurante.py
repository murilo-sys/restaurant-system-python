import os
import time

from services import restaurante_services

nome = input("Digite o nome do restaurante \n")
os.system("cls")

restaurante = restaurante_services.Restaurante(nome)

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
            preco_produto = float(input("Insira o preço do produto\nR$"))
            restaurante.registrarVenda(preco_produto)

