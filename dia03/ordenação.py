#%%
import pandas as pd

# %%
df = pd.read_csv('../data/customers.csv', sep=';')
df

# %%
df = (df.sort_values(by=['Points', 'Name'], ascending=False)
        .rename(columns={'UUID': 'id',
                         'Name': 'nome',
                         'Points': 'pontos'}))
df