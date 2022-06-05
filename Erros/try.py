from math import *
from data import final_calculate

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

x_sup = x_gap[1]
x_inf = x_gap[0]
#Mapeamento do intervalo y
y_gap = []
for i in range(2):
    if i == 0:
        border = "inferior" 
    else:
        border = "superior"
    value_gap = input(f'Digite o intervalo {border} mais externo: ')
    y_gap.append(value_gap)
y_sup = y_gap[1]
y_inf = y_gap[0]
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

#Tratando os dados
x_j_copy = x_j.copy()
w_j_copy = w_j.copy()
for i in range(len(x_j)):
    index = -1-i
    x_j_copy.append((x_j[index])*(-1))
    w_j_copy.append(w_j[index])
x_j=x_j_copy
w_j=w_j_copy
print(x_j)
print(w_j)
sum_functions_y = []
for i in range(len(x_j)):
    x_i = '(1/2)*(((y_sup - y_inf)*('+str(x_j[i])+'))+(y_sup + y_inf))'
    new_function = function
    new_function = '('+new_function.replace('y', x_i)+')*((y_sup - y_inf)/2)*'+str(w_j[i])
    sum_functions_y.append(new_function)
sum_functions_x = []
x_i_map=[]
for i in range(len(sum_functions_y)):
    for i in range(len(x_j)):
        x_i = str(eval('(1/2)*(((x_sup - x_inf)*('+str(x_j[i])+'))+(x_sup + x_inf))'))
        new_function = sum_functions_y[i]
        new_function = new_function.replace('y_sup', y_sup)
        new_function = new_function.replace('y_inf', y_inf)
        new_function = str(eval('('+new_function.replace('x', x_i)+')*((x_sup - x_inf)/2)*'+str(w_j[i])))
        sum_functions_x.append(new_function)
        print(new_function)
        x_i_map.append(x_i)
        
geral_result = 0
for i in range(len(sum_functions_x)):
    f_calc = sum_functions_x[i]
    x=x_i_map[i]
    expression = eval(f_calc)

    geral_result = geral_result + expression

print(geral_result)