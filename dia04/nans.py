# %%
import pandas as pd
import numpy as np

# %%
data = {
    'nome': ['Téo', 'Nah', 'Lah', 'Mah', 'Jo'],
    'idade': [31, 32, 34, 12, np.nan],
    'renda': [np.nan, 3245, 357, 12432, np.nan]
}

# %%
df = pd.DataFrame(data)
df

# %%
# Quantos NA na coluna 'idade'?
df['idade'].isna().sum()

# %%
# Quantos NA no DataFrame?
df.isna().sum()

# %%
# Qual o percentual de NA no DataFrame?
df.isna().mean()

# %%
df.fillna({
    'idade': df['idade'].mean(),
    'renda': df['renda'].mean()
    })

# %%
df.dropna()

# %%
df.dropna(how='all')

# %%
df.dropna(subset=['idade', 'renda'], how='all')

# %%
df.dropna(axis=1, how='any')

# %%
df.dropna(axis=1, thresh=3)

# %%
df.dropna(axis=1, thresh=4)

# %%
df.dropna(axis=1, thresh=5)

# %%
