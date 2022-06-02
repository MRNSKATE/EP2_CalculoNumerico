from math import *
from data import datas

names = {'sqrt': sqrt, 'pow': pow}

function = input("Digite uma função: ")
n = int(input("Digite a quantidade de nós: "))
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
#Obtendo x_gap negativo
x_gap_negative=[]
for i in range(len(x_gap)):
    x_gap_new = (-1.0)*float(x_gap[i])
    x_gap_negative.append(x_gap_new)
#Mapeamento do intervalo y
y_gap = []
for i in range(2):
    if i == 0:
        border = "inferior" 
    else:
        border = "superior"
    value_gap = input(f'Digite o intervalo {border} mais externo: ')
    y_gap.append(value_gap)
#Obtendo y_gap negativo
y_gap_negative=[]
for i in range(len(y_gap)):
    y_gap_new = "-"+y_gap[i]
    y_gap_negative.append(y_gap_new)
#Mapeando o valor de yi e substituindo na fórmula
if n == 6:
    x_j =  [0.2386191860831969086305017, 0.6612093864662645136613996, 0.9324695142031520278123016]
    w_j = [0.4679139345726910473898703, 0.3607615730481386075698335, 0.1713244923791703450402961]
elif n== 8:
    x_j = [0.1834346424956498049394761, 0.5255324099163289858177390, 0.7966664774136267395915539, 0.9602898564975362316835609]
    w_j = [0.3626837833783619829651504, 0.3137066458778872873379622, 0.2223810344533744705443560, 0.1012285362903762591525314]
else:
    x_j= [0.1488743389816312108848260,0.4333953941292471907992659, 0.6794095682990244062343274, 0.8650633666889845107320967, 0.9739065285171717200779640]
    w_j= [0.2955242247147528701738930, 0.2692667193099963550912269, 0.2190863625159820439955349, 0.1494513491505805931457763, 0.0666713443086881375935688]

sum_functions_y = []
i = 0
while i < n:
    if i < n/2:
        loop_x_j = str(x_j[i])
        loop_w_j = str(w_j[i])
        x_i = "(1/2)*((y_gap[1] + y_gap_negative[0])*"+loop_x_j+"+(y_gap[1] + y_gap[0]))"
        newfunction = function.replace('y', x_i)+"*"+loop_w_j+"*(y_gap[1] + y_gap_negative[0])/2"
        sum_functions_y.append(newfunction)
    else:
        index = int((n/2)-i-1)
        loop_x_j = str(x_j[index])
        loop_w_j = str(w_j[index])

        x_i = "(1/2)*((y_gap[1] + y_gap_negative[0])*"+loop_x_j+"+(y_gap[1] + y_gap[0]))"
        newfunction = function.replace('y', x_i)+"*"+loop_w_j+"*(y_gap[1] + y_gap_negative[0])/2"
        sum_functions_y.append(newfunction)
    i = i + 1

#Mapeando o valor de xi e substituindo na fórmula

sum_functions_x = []
for j in range(len(sum_functions_y)):
    i=0
    while i < n:
        if i < n/2:
            loop_x_j = str(x_j[i])
            loop_w_j = str(w_j[i])
            x_i = "(1/2)*((x_gap[1] + x_gap_negative[0])*"+loop_x_j+"+(x_gap[1] + x_gap[0]))"
            newfunction = sum_functions_y[i].replace('x', x_i)+"*"+loop_w_j+"*(x_gap[1] + x_gap_negative[0])/2"
            sum_functions_x.append(newfunction)
        else:
            index = int((n/2)-i-1)
            loop_x_j = str(x_j[index])
            loop_w_j = str(w_j[index])

            x_i = "(1/2)*((x_gap[1] + x_gap_negative[0])*"+loop_x_j+"+(x_gap[1] + x_gap[0]))"
            newfunction = sum_functions_y[index].replace('x', x_i)+"*"+loop_w_j+"*(x_gap[1] + x_gap_negative[0])/2"
            sum_functions_x.append(newfunction)
        i = i + 1

def calculando_final(sum_functions_x, x_gap, y_gap):
    somatorio = 0
    for i in range(len(sum_functions_x)):
        #somatorio = somatorio + eval(sum_functions_x[i])
        print(eval(sum_functions_x[i]))
    return somatorio
print(sum_functions_x)
print(x_gap)
print(y_gap)
print(calculando_final(sum_functions_x, x_gap, y_gap))
'''for i in range(len(sum_functions_x)):
    number = eval(sum_functions_x[i])
    print(number)'''
