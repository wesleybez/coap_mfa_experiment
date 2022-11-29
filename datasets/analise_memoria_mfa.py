import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import timeit

#pd.options.plotting.backend = 'plotly'
#matplotlib inline

cols_memory=['nro', 'initial', 'final', 'used']
cols_time=['nro', 'initial', 'connection', 'publish', 'subscribe','disconnect']

pd.set_option("display.max.columns", None)

df_memory_10    = pd.read_csv('20210514_10_coap_memory_proposta.csv',names=cols_memory,header=None)
df_memory_100  = pd.read_csv('20210514_100_coap_memory_proposta.csv',names=cols_memory,header=None)
df_memory_200  = pd.read_csv('20210514_200_coap_memory_proposta.csv',names=cols_memory,header=None)


#print(df.to_string())
print("\nmemory")
print("\n10")
print(df_memory_10[['used']].describe(include='all'))
print("\n100")
print(df_memory_100[['used']].describe(include='all'))
print("\n200")
print(df_memory_200[['used']].describe(include='all'))
