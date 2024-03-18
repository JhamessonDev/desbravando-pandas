#%%
import pandas as pd

# %%
idades = [30, 42, 90, 34]
idades

# %%
media = sum(idades) / len(idades)

total = 0
for i in idades:
    total += (media - i) ** 2

variancia = total /(len(idades) - 1)

variancia

# %%
# Transformação para Series Pandas
series_idades = pd.Series(idades)
series_idades

# %%
# --- MÉTODOS DA SERIES PANDAS --

# Média
series_idades.mean()

# %%
# Variância
series_idades.var()

#%%
# Desvio padrão
series_idades.std()

# %%
# Mediana
series_idades.median()

# %%
# 3o Quartik
series_idades.quantile(0.75)

# %%
# Sumarizaçao
series_idades.describe()

# %%
# Dimensão da Series
series_idades.shape

# %%
# Navagando na lista
idades[0]

# %%
series_idades.index

# %%
# Alterando index da Series
series_idades.index = ['j', 'h', 'a', 'm']

# %%
# Navegando no índices novos
series_idades['j']

# %%
series_idades.iloc[0]

# %%
series_idades.iloc[0:2]

# %%
# Atrubuindo um nome pada a Series
series_idades.name = 'idades'
series_idades
# %%
