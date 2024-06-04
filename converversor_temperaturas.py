class ConversorTemperatura:
    def __init__(self):
        pass

    def celsius_to_fahrenheit(celsius):
     return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(fahrenheit):
     return (fahrenheit - 32) * 5/9

    print("Escolha a conversão que deseja realizar:")
    print("1: Celsius para Fahrenheit")
    print("2: Fahrenheit para Celsius")
    escolha = input("Digite 1 ou 2: ")

    if escolha == "1":
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} graus Celsius é igual a {fahrenheit} graus Fahrenheit.")
    elif escolha == "2":
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} graus Fahrenheit é igual a {celsius} graus Celsius.")
    else:
        print("Escolha inválida. Por favor, digite 1 ou 2.")
