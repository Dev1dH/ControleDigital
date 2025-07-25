import numpy as np

#função em python para implementar o Critério de Jury
def metodo_jury(a):
    
    a = np.array(a, dtype=float)
    n = len(a) - 1

    # Condição 0: a[0] > 0
    if a[0] <= 0:
        print("Falha na condição a[0] > 0")
        return False

    # Condição 1: |a[n]| < a[0]
    if abs(a[-1]) >= a[0]:
        print("Falha na condição |a[n]| < a[0]")
        return False

    # Condição 2: |P(1)| > 0
    if abs(np.sum(a)) <= 0:
        print("Falha na condição |P(1)| > 0")
        return False

    # Condição 3: |P(-1)| > 0
    if abs(np.sum(a * (-1) ** np.arange(n + 1))) <= 0:
        print("Falha na condição |P(-1)| > 0")
        return False

    # Construção da Tabela de Jury
    J = [a, np.flip(a)]

    k = 0
    while len(J[k]) > 2:
        prev_row = J[k]
        next_row = J[k + 1]
        new_len = len(prev_row) - 1
        new_row = []

        for i in range(new_len):
            val = prev_row[0] * next_row[i + 1] - prev_row[-1] * next_row[i]
            new_row.append(val)
        
        denom = prev_row[0] - prev_row[-1]
        if denom == 0:
            print("Divisão por zero na construção da tabela.")
            return False

        new_row = np.array(new_row) / denom
        J.append(new_row)
        k += 2

    # Se passou por todas as etapas retorna o valor verdadeiro, ou seja, é estável:
    return True

#coeficiente da funçao em malha fechada
coeficientes = [1.011, -1.601, 0.6757]

#verificar se o sistema é estável ou instável
if metodo_jury(coeficientes):
    print("O sistema é estável.")
else:
    print("O sistema é instável.")