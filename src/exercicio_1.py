import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('../data/census.csv')

# O histograma baseado nos intervalos padrões criados pelo Pandas mostrou que não foi uma boa distribuição.
# O Jones mostrou na solução do exercício uma maneira de criar intervalos manuais e é essa solução que coloquei
# abaixo.
dataset['age'] = pd.cut(dataset['age'], bins=[0,17,25,40,60,90],
                        labels=['Faixa 1','Faixa 2','Faixa 3','Faixa 4','Faixa 5'])
# Jones não mostrou como plotar os dados do DataFrame depois que ele fez a organização por faixas.
# A linha abaixo eu defini depois de algumas pesquisas na internet.
dataset['age'].value_counts().plot(ylabel='Número de Pessoas',kind='bar');
plt.show()
