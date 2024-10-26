import pandas as pd

import numpy as np

import os
os.system('cls')

df = pd.read_excel('vendas_roupas.xlsx')
print('Exibindo as 10 primeiras linhas')
print(df.head(10))

media = np.mean(df['Preço por Unidade (R$)'])
print('Esse é o preço médio por unidade')
print(media)

faturamento = df.head(10)['Faturamento Total (R$)']
maior_fatu = faturamento.max()

print('Esse é o maior faturamento entre os 10 primeiros itens')
print(maior_fatu)

menor_fatu = faturamento.min()
print('Esse é o menor faturamento entre os 10 primeiros itens')
print(menor_fatu)

satis = df.head(10)[df['Satisfação'] == 'Baixo']
print('Esse(s) é(são) o(s) produto(s) de satisfação baixa')
print(satis)

total = faturamento.sum()
print('Esse é o somatorio total da quantidade de vendas')
print(total)