def menu_principal():
    print("\n**Calculadora de Conversão de Unidades**")
    print("1. Converter Comprimento")
    print("2. Converter Temperatura")
    print("3. Sair")
    opção = (input("Digite a opção desejada: "))
    return opção
def sair():
    print("Encerrando o programa...")
escolha = menu_principal()

if escolha == "1":
   from conversor_medidas import ConversorMedidas
elif escolha == "2":
   from converversor_temperaturas import ConversorTemperatura
elif escolha == "3":
    sair()
else:
    print("Opção não existente, tente novamente")