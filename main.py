from conversor_medidas import ConversorMedidas
from converversor_temperaturas import ConversorTemperatura
def menu_principal():
    while True:
        print("\n*Calculadora de Conversão de Unidades*")
        print("1. Converter de centímetros para metros")
        print("2. Converter de metros para centímetros")
        print("3. Converter de celsius para fahrenheit")
        print("4. Converter de fahrenheit para celsius")   
        print("5. Sair")
        opção = str(input("Digite a opção desejada: "))
        if opção == "5":
            break
        valor = float(input("Digite o seu valor:  "))
        if opção == "1":
            valor = ConversorMedidas.cm_to_m(valor)
        elif opção == "2":
            valor = ConversorMedidas.m_to_cm(valor)
        elif opção == "3":
            valor= ConversorTemperatura.celsius_to_fahrenheit(valor)
        elif opção == "4":
            valor= ConversorTemperatura.fahrenheit_to_celsius(valor)
        else:
            print("Opção inválida. Tente novamente.")
        print('Resultado:   ',valor)

menu_principal()