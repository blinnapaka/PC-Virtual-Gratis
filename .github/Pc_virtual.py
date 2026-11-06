import os
import time
import platform

usuario = "Admin"
arquivos = []
ligado = True

def inicializar():
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 40)
    print("       MEU PC VIRTUAL")
    print("=" * 40)
    print("Sistema iniciado com sucesso!")
    print("Bem-vindo,", usuario)

def informacoes():
    print("\n--- INFORMAÇÕES DO PC ---")
    print("Usuário:", usuario)
    print("Sistema:", platform.system())
    print("Processador:", platform.processor())
    print("Arquitetura:", platform.machine())

def bloco_notas():
    texto = input("Digite uma anotação: ")
    arquivos.append(texto)
    print("Arquivo salvo!")

def visualizar():
    print("\n--- MEUS ARQUIVOS ---")
    if not arquivos:
        print("Nenhum arquivo encontrado.")
    for i, arquivo in enumerate(arquivos):
        print(i + 1, "-", arquivo)

def calculadora():
    n1 = float(input("Primeiro número: "))
    op = input("Operação (+,-,*,/): ")
    n2 = float(input("Segundo número: "))
    if op == "+":
        print("Resultado:", n1 + n2)
    elif op == "-":
        print("Resultado:", n1 - n2)
    elif op == "*":
        print("Resultado:", n1 * n2)
    elif op == "/" and n2 != 0:
        print("Resultado:", n1 / n2)
    else:
        print("Operação inválida!")

inicializar()
while ligado:
    print("\n===== ÁREA DE TRABALHO =====")
    print("1 - Informações do PC")
    print("2 - Bloco de notas")
    print("3 - Meus arquivos")
    print("4 - Calculadora")
    print("5 - Desligar PC")
    opcao = input("\nEscolha uma opção: ")
    if opcao == "1":
        informacoes()
    elif opcao == "2":
        bloco_notas()
    elif opcao == "3":
        visualizar()
    elif opcao == "4":
        calculadora()
    elif opcao == "5":
        print("Desligando o PC...")
        time.sleep(2)
        ligado = False
    else:
        print("Opção inválida!")
print("PC Virtual desligado. Até logo!")
