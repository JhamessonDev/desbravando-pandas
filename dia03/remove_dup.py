#%%
import pandas as pd

# %%
data = {
    'nome': ['Téo', 'Nah', 'Maria', 'Nah', 'Lara', 'Téo'],
    'idade': [32, 33, 2, 33, 31, 32],
    'updated_at': [1, 2, 3, 1, 2, 3]
}

df = pd.DataFrame(data)
df

# %%
df = df.drop_duplicates()
df
# %%
df = df.sort_values(by='updated_at', ascending=False)
df

# %%
df = df.drop_duplicates(subset=['nome', 'idade'], keep='first')
df

# %%
df = (df.sort_values(by='updated_at', ascending=False)
        .drop_duplicates(subset=['nome', 'idade'], keep='first'))
df
# %%
