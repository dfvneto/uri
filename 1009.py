nome=input()
salario=float(input())
vendas=float(input())
percentual = 15
percentual_calculado = 15/100
salario_total = percentual_calculado*vendas + salario
print("TOTAL = R$ %.2f" % salario_total)