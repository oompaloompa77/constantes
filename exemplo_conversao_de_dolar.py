#Definição da constante para a taxa de câmbio
DOLAR = 5.50

valor_em_dolar = float(input("Digite o valor em dólar: "))
valor_em_real = valor_em_dolar * DOLAR
print(F"O valor convertido em reais é: R$ {valor_em_real:.2f}")
