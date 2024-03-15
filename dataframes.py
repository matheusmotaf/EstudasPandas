import pandas as pd


dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
print(dados)
series = pd.Series(dados)
#print(series)

# %%
media = series.mean()
print(media)

# %%
desvio = series.std()
print(desvio)

# %%
maximo = series.max()
print(maximo)