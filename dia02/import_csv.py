#%%
import pandas as pd

# %%
df_customers = pd.read_csv('../data/customers.csv', sep=';')
df_customers.head()

# %%
df_customers.shape

# %%
df_customers.info(memory_usage='deep')

# %%
df_customers['Points'].astype(int)
# %%
df_customers['Points'].describe()

# %%
condicao = df_customers['Points'] > 1000

df_customers[condicao]

# %%
condicao = df_customers['Points'] == df_customers['Points'].max()
df_customers[condicao]

# %%
df_customers['Points'] == df_customers['Points'].max()

# %%
df_customers[df_customers['Points'] == df_customers['Points'].max()]['Name']

# %%
df_customers[df_customers['Points'] == df_customers['Points'].max()]['Name'].iloc[0]

# %%
condicao = df_customers['Points'] == df_customers['Points'].max()
df_maior = df_customers[condicao]
df_maior['Name'].iloc[0]

# %%
condicao = (df_customers['Points'] >= 1000) & (df_customers['Points'] <= 2000)
df_customers[condicao]

# %%
colunas = ['UUID', 'Name']

df_customers[colunas]

#%%
colunas = list(df_customers.columns)
colunas

# %%
colunas = df_customers.columns.to_list()
colunas.sort()
colunas 

df_customers[colunas]

# %%
df_customers = df_customers.rename(columns={'Name': 'Nome',
                                            'Points': 'Pontos'})
df_customers

# %%
df_customers.rename(columns={'UUID': 'Id'}, inplace=True)
df_customers
