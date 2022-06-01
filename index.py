from math import *
from date import dates

names = {'sqrt': sqrt, 'pow': pow}

function = input("Digite uma função: ")
n = input("Digite a quantidade de nós: ")
possible_n = [6, 8, 10]

#Mapeamento do intervalo x
x_gap = []
for i in range(2):
    if i == 0:
        border = "inferior" 
    else:
        border = "superior"
    value_gap = float(input(f'Digite o intervalo {border} mais externo: '))
    x_gap.append(value_gap)

#Mapeamento do intervalo y
y_gap = []
for i in range(2):
    if i == 0:
        border = "inferior" 
    else:
        border = "superior"
    value_gap = input(f'Digite o intervalo {border} mais externo: ')
    y_gap.append(value_gap)

#Mapeando o valor de yi e substituindo na fórmula
x_j, w_j = dates(n)

sum = []
i = 0
while i < len(x_j):
    if i < len(x_j)/2 - 1:
        x_i = "(1/2)*((y_gap[1] - y_gap[0])*"+str(x_j[i])+"+((y_gap[1] + y_gap[0]))"
        newfunction = function.replace('y', x_i)+"*"+str(w_j[i])+"(y_gap[1] - y_gap[0])/2"
        sum.append(newfunction)
    else:
        x_i = "(1/2)*((y_gap[1] - y_gap[0])*"+str(x_j[i-len(x_j)/2-1])+"+((y_gap[1] + y_gap[0]))"
        newfunction = function.replace('y', x_i)+"*"+str(w_j[i-len(x_j)/2-1])+"(y_gap[1] - y_gap[0])/2"
        sum.append(newfunction)
    i = i + 1

print(sum)