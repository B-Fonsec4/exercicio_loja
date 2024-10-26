import pandas as pd

roupas = ['Camiseta', 'Calça', 'Jaqueta' , 'Vestido', 'Boné']
quantidade = [50,30,15,10,25]

estoque = pd.Series(quantidade, index= roupas)
print('Serie estoque de roupas')
print(estoque)

# adicionando saio com none

estoque.loc['Saia'] = None
print('Adicionda roupa fora do estoque')
print(estoque)

print( 'roupas com mais de 20 em estoque')
print(estoque[estoque >20])

precos = pd.Series([3500,2500,1200,900,1500], index=roupas)
print('Precos das roupas em estoque')
print(precos)

print('valor total do estoque por roupa (preço * quantidade): ')
print(precos * quantidade)