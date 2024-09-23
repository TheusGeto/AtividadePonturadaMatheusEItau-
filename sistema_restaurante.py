"""
Informe o número da turma: 
Turma - 

Nome completo dos componentes.
1 - Itauã GUALBERTO.
2 - 
"""
total = 0
import os
os.system("cls || clear") 

# Limpa o terminal.

while True:
    print("""
    1- filé
    2- macarrão
    3- arroz e feijão
    4- mocotó
    5- salada
    6- lasanha
    7- strogonoff 
    """)

    prato = input("faça sua escolha acima: ")
    match(prato):
        case "1":
            total += 7.50
            print("filé = $7,50")
        case "2":
            total += 5.0
            print("macarrão = $5,00")
        case "3":
            total += 10.50
            print("arroz e feijão = $10,50")
        case "4":
            total += 14.99
            print("mocotó = $14,99 ")
        case "5":
            total += 3.24
            print("salada = $3,24")
        case "6":
            total += 15.50
            print("lasanha = $15,.50")
        case "7":
            total += 17.75
            print("lasanha = $17,75")
        case _: 
            print("resposta invalida burrão!!!")
    while True:
        continuar = input("quer acrescentar mais pratos: [SIM(S)/NÃO(N)] ").strip().upper()
        if continuar in ['S', 'N']:
            break
        else:
            print("resposta inválida!!!")
    
    # Saindo do loop se a resposta for 'N'
    if continuar == 'N':
        break

print(f"Total a pagar: R${total:.2f}")