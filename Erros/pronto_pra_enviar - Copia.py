#### Exercício Programa 1 – MAP2220 – Fundamentos de Análise Numérica
### Grupo: 
### Bárbara Gomes Prearo - 11202301
### Danilo dos Santos Dantas - 11871434
### Diego Pereira Peres - 11298466

import numpy as np

### A função Legen(n) vai retornar os zeros dos polinomios da familia de Legendre, que são ortogonais no intervalo [-1,1]
### Os valores para n especificados foram n=6, n=8 e n=10 pontos
### Abaixo segue a função com a especificação de valores do polinômio para cada valor de n 
        
def Legen(n):  

    if n == 6:
        return [[0.2386191860831969086305017, 0.4679139345726910473898703], [0.6612093864662645136613996, 0.3607615730481386075698335],[0.9324695142031520278123016, 0.1713244923791703450402961]]

    if n == 8:
        return [[0.1834346424956498049394761, 0.3626837833783619829651504],[0.5255324099163289858177390, 0.3137066458778872873379622], [0.7966664774136267395915539, 0.2223810344533744705443560], [0.9602898564975362316835609, 0.1012285362903762591525314]]

    if n == 10:
        return [[0.1488743389816312108848260, 0.2955242247147528701738930], [0.4333953941292471907992659, 0.2692667193099963550912269],[0.6794095682990244062343274, 0.2190863625159820439955349], [0.8650633666889845107320967, 0.1494513491505805931457763], [0.9739065285171717200779640, 0.0666713443086881375935688]]

### A função integral recebe 4 parâmetros a fim de retornar um valor aproximado do resultado do cálculo da integral em questão 
### O primeiro parâmetro é a função [f] que se deseja integrar
### O segundo parâmetro é uma lista [limite_da_primeira_integral], que reune os valores dos limites da primeira integral 
### O terceiro parâmetro é a lista [limite_da_segunda_integral] que reune os valores do intervalo considerado para o cálculo da segunda integral 
### O quarto parâmetro é o valor de n
### O resultado que a função retorna equivale a aproximação para a integral calculada 

def integral(f, limite_da_primeira_integral, limite_da_segunda_integral, n):
    x_inf, x_sup = limite_da_segunda_integral[0], limite_da_segunda_integral[1]
    auxiliar_sub = (x_sup-x_inf)/2
    auxiliar_sum = (x_sup+x_inf)/2
    Resultado = 0 
    for i in range(n):
        if i < n/2:
            R = 0
            L = Legen(n)[(int)(n/2)-(i+1)]
            x = -auxiliar_sub*L[0] + auxiliar_sum
            e = limite_da_primeira_integral[1](x)
            g = limite_da_primeira_integral[0](x)
            k1 = (e-g)/2
            k2 = (e+g)/2
        else:
            R = 0
            L = Legen(n)[(int)(i %(int) (n/2))]
            x = auxiliar_sub*L[0] + auxiliar_sum
            e = limite_da_primeira_integral[1](x)
            g = limite_da_primeira_integral[0](x)
            k1 = (e-g)/2
            k2 = (e+g)/2            
        
        for contador_j in range(n):
            if contador_j < n/2:
                y = k1*(-Legen(n)[(int)(n/2)-(contador_j+1)][0]) + k2
                Q = f(x,y)
                R = R + Legen(n)[(int)(n/2)-(contador_j+1)][1]*Q
            else:
                y = k1*(Legen(n)[(int)(contador_j % (int)(n/2))][0]) + k2
                Q = f(x,y)
                R = R + Legen(n)[(int)(contador_j % (int)(n/2))][1]*Q
        if i < n/2:
            Resultado = Resultado + Legen(n)[(int)(n/2)-(i+1)][1]*k1*R*auxiliar_sub
        else:
            Resultado = Resultado + Legen(n)[(int)(i % (int)(n/2))][1]*k1*R*auxiliar_sub
    return Resultado
    
### A função volume_cubo calcula o volume do cubo de aresta 1 pedido no Exemplo 1 do enunciado
def volume_cubo(n_nos):
    
    f = lambda x, y : 1
    zx = lambda x : 0
    wx = lambda x : 1
    
    Volume_do_cubo = integral(f, [zx, wx], [0,1], n_nos)
    
    return Volume_do_cubo

### A função volume_tetraedro calcula o volume do tetraedro de vertices (0; 0; 0), (1; 0; 0), (0; 1; 0) e (0; 0; 1) pedido no Exemplo 1 do enunciado
def volume_tetraedo(n_nos):
    
    f = lambda x,y : 1-x-y
    zx = lambda x : 0
    wx = lambda x : 1-x
    
    Volume_do_tetraedro  = integral(f, [zx, wx], [0,1], n_nos)
    
    return Volume_do_tetraedro

### A função primeira_integral calcula a primeira integral dydx apresentada no enunciado 
def primeira_integral(n_nos):
    
    f   = lambda x, y : 1
    zx = lambda x : 0
    wx = lambda x : 1 - x ** 2
    
    Area_da_Parabola_integral_1 = integral(f, [zx, wx], [0,1], n_nos)
    
    return Area_da_Parabola_integral_1
    
### A função segunda_integral calcula a segunda integral dxdy apresentada no enunciado 
def segunda_integral(n_nos):

    # Houve uma mudança da orientação pela mudança da ordem das integrais, em que a segunda é dxdy
    # Como o código funciona para variações em X, mudou-se a orientação da parábola 
    
    f = lambda x, y : 1
    zx = lambda x : 0
    wx = lambda x : np.sqrt(1 - x)
    
    Area_da_Parabola_integral_2 = integral(f, [zx, wx], [0,1], n_nos)
    
    return Area_da_Parabola_integral_2

### A função volume_3 calcula o volume da região abaixo da superfície descrita pela equação z=e^(y/x), apresentada no enunciado 
def volume_3(n_nos):
    
    # Cálculo do volume
    f = lambda x, y : np.exp(y/x)
    zx = lambda x : x ** 3
    wx = lambda x : x ** 2

    Volume = integral(f, [zx, wx], [0.1, 0.5], n_nos)
    
    return Volume

### A função area_3 calcula a area da região abaixo da superfície descrita pela equação z=e^(y/x), apresentada no enunciado 
def area_3(n_nos):
        # Cálculo da área
    f = lambda x, y : np.sqrt((np.exp(2*y/x)/x**2) * (y**2/x**2 + 1) + 1)
    zx = lambda x : x ** 3
    wx = lambda x : x ** 2

    Area = integral(f, [zx, wx], [0.1, 0.5], n_nos)
    
    return Area
    
### A função volume_calota calcula o volume da calota esférica de altura 1/4 da esfera de raio 1 gerada pela rotação de uma região R em torno de uma reta gama, dados no enunciado
def volume_calota(n_nos):
    f = lambda x, y : y
    zx = lambda x : 0
    wx = lambda x : np.sqrt(1-(x+(3/4))**2)
    Volume_calota = 2*np.pi*integral(f, [zx, wx], [0, 0.25], n_nos)
    
    return Volume_calota

# A função volume_solido_revolução calcula o volume do sólido de revolução obtido pela rotação de uma região R em torno de uma reta gama, dados no enunciado
def volume_solido_revolução(n_nos):
    
    f = lambda x, y : y
    zx = lambda x : 0
    wx = lambda x : np.exp(-(x**2))

    Volume_solido_revolução = 2*np.pi*integral(f, [zx, wx], [-1, 1], n_nos)
    
    return Volume_solido_revolução

#A função apresenta os resultados do Exemplo 1: Cálculo os volumes do cubo com aresta de comprimento 1 e do tetraedro de vertices (0; 0; 0), (1; 0; 0), (0; 1; 0) e (0; 0; 1)
def ex_1():
    
    print("\n EXEMPLO 1: \n")
    
    print("Cálculo dos volumes dos cubos de aresta 1 de acordo com o número de nós \n")
   
    n_6 = volume_cubo(6)
    print ("O volume do cubo de aresta 1 considerando 6 nós é:", n_6)
    n_8 = volume_cubo(8)
    print("O volume do cubo de aresta 1 considerando 8 nós é: ", n_8)
    n_10 = volume_cubo(10)
    print("O volume do cubo de aresta 1 considerando 10 nós é: ", n_10,"\n")
    
    print("Cálculo dos volumes dos tetraedros de acordo com o número de nós \n")
    
    n_6 = volume_tetraedo(6)
    print("O volume do tetraedro considerando 6 nós é: ", n_6)
    n_8 = volume_tetraedo(8)
    print("O volume do tetraedro considerando 8 nós é: ", n_8)
    n_10 = volume_tetraedo(10)
    print("O volume do tetraedro considerando 10 nós é: ", n_10, "\n")

#A função apresenta os resultados do Exemplo 2: Cálculo da area A da região do primeiro quadrante definido pelos eixos do primeiro quadrante e pela curva y=1-x^2 (Parábola)
def ex_2():

    print("\n EXEMPLO 2: \n")
    
    print("Cálculo da primeira integral (dydx) apresentada no enunciado \n")
    
    n_6 = primeira_integral(6)
    print("A área pela primeira integral considerando 6 nós é: ", n_6)
    n_8 = primeira_integral(8)
    print("A área pela primeira integral considerando 8 nós é: ", n_8)
    n_10 = primeira_integral(10)
    print("A área pela primeira integral considerando 10 nós é: ", n_10,"\n")
    
    print("Cálculo da segunda integral (dxdy) apresentada no enunciado \n")
    
    n_6 = segunda_integral(6)
    print("A área pela segunda integral considerando 6 nós é: ", n_6)
    n_8 = segunda_integral(8)
    print("A área pela segunda integral considerando 8 nós é: ", n_8)
    n_10 = segunda_integral(10)
    print("A área pela segunda integral considerando 10 nós é: ", n_10, "\n")
 
#A função apresenta os resultados do Exemplo 3: Cálculo da área e do volume da superfície descrita por z=e^(y/x)   
def ex_3():

    print("\n EXEMPLO 3:\n")
    
    print("Cálculo da área da superfície descrita por z=e^(y/x) \n")
    
    n_6 = area_3(6)
    print("A área calculada para a superfície utilizando 6 nós é: ", n_6)
    n_8 = area_3(8)
    print("A área calculada para a superfície utilizando 8 nós é: ", n_8)
    n_10 = area_3(10)
    print("A área calculada para a superfície utilizando 10 nós é: ", n_10, "\n")
    
    print("Cálculo do volume da superfície descrita por z=e^(y/x) \n")
    
    n_6 = volume_3(6)
    print("O Volume encontrado abaixo da superfície dada, considerando 6 nós é: ", n_6)
    n_8 = volume_3(8)
    print("O Volume encontrado abaixo da superfície dada, considerando 8 nós é: ", n_8)
    n_10 = volume_3(10)
    print("O Volume encontrado abaixo da superfície dada, considerando 10 nós é: ", n_10)

### A função apresenta os resultados do Exemplo 4: Cálculo do volume da calota e do sólido de revolução gerados pela rotação de uma região R em torno de uma reta gama
def ex_4():
    
    print("\n EXEMPLO 4:\n")
    
    print("Cálculo do volume da calota \n")
    
    n_6 = volume_calota(6)
    print("O volume da calota considerando 6 nós é: ", n_6)
    n_8 = volume_calota(8)
    print("O volume da calota considerando 8 nós é: ", n_8)
    n_10 = volume_calota(10)
    print("O volume da calota considerando 10 nós é: ", n_10, "\n")
    
    print("Cálculo do volume do sólido (inteiro) de revolução \n")
    
    n_6 = volume_solido_revolução(6)
    print("O Volume do sólido de revolução considerando 6 nós é: ", n_6)
    n_8 = volume_solido_revolução(8)
    print("O Volume do sólido de revolução considerando 8 nós é: ", n_8)
    n_10 = volume_solido_revolução(10)
    print("O Volume do sólido de revolução considerando 10 nós é: ", n_10)
    
if __name__ == "__main__":
    
    ex_1()
    ex_2()
    ex_3()
    ex_4()
