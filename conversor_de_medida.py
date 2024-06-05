def cm_para_metros(cm):
    metros = cm / 100
    return metros

# Solicitando a entrada do usuário para o valor em centímetros
centimetros = float(input("Digite o valor em centímetros: "))

# Chamando a função para converter centímetros em metros
resultado = cm_para_metros(centimetros)

# Exibindo o resultado da conversão
print(f"{centimetros} centímetros equivalem a {resultado} metros.")
