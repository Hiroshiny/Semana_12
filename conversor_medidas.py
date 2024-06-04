class ConversorMedidas:
    def __init__(self):
        pass

    def cm_to_m(cm):
     return cm / 100

    def m_to_cm(m):
     return m * 100

    print("Escolha a conversão que deseja realizar:")
    print("1: Centímetros para Metros")
    print("2: Metros para Centímetros")
    escolha = input("Digite 1 ou 2: ")

    if escolha == "1":
      conversor = float(input("Digite a quantidade em centímetros que deseja converter para metros:\n")) / 100
      print(f"O valor convertido é {conversor} metros.")
    elif escolha == "2":
       conversor = float(input("Digite a quantidade em metros que deseja converter para centímetros:\n")) * 100
       print(f"O valor convertido é {conversor} centímetros.")
    else:
        print("Escolha inválida. Por favor, digite 1 ou 2.")


