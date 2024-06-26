print(f" Menu Principal ".center(26,"="))
menu = """
[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

"""
print("=".center(26,"="))
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input (menu)
    sair_pagina = 1
 # Operação de Deposito:
    if opcao == "d":
      print(" Deposito ".center(30,"="))
      while sair_pagina >=1 or sair_pagina <=2:
        if sair_pagina == 1:       
          deposito = float(input ("Informe o Valor para Deposito: " ))             
          if deposito > 0:
             saldo += deposito
             extrato += f"Depósito: R$ {deposito:.2f}\n"   
             sair_pagina = int(input("\nRealizar outro Deposito?\n[1] Sim\n[2] Não\n"))                 
          else: 
             print("Saldo de Deposito Invalido")
        elif sair_pagina==2:
            print("Voltando ao Menú...")
            break
        else:
             print("Opção Invalida")
             break

      else:
          break
          
 # Operação de Saque:
    elif opcao == "s":
      print(" Saque ".center(31,"="))
      saque = float(input("\nQual o Valor de Saque: \n"))
      saldo_exedeu = saque > saldo
      limite_exedeu = saque > limite
      saque_exedeu = numero_saques >= LIMITE_SAQUES
      if saldo_exedeu:
             print("Falha na Operação por Saque ser Maior que o Saldo! ")
         
      elif limite_exedeu:
             print("Falha na Operação por Execeder Limite de Saque ") 

      elif saque_exedeu:
             print("Falha na Operação por Execeder Quantidade de Saques Diários")       

      elif saque > 0:
             saldo -= saque
             extrato += f"Saque: R$ {saque:.2f}\n"
             numero_saques += 1 

      else:
             print("Falha na operação por Valor Invalido")    
           
 # Operação Extrato  
    elif opcao == "e":
        print (" Extrato ".center(35,"="))
        print(extrato)
        print("-".center(35,"-"))
        print(f"Saldo Atual da Conta: R${saldo:.2f}")
        print("=".center(35,"="))
     
    
    elif opcao == "q":
        break

    else:
        print("Opção Invalida!")
