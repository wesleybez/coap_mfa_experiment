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

df_memory_auth_10    = pd.read_csv('20210514_10_coap_memory_autenticated.csv',names=cols_memory,header=None)
df_memory_noauth_10  = pd.read_csv('20210514_10_coap_memory_non_auth.csv',names=cols_memory,header=None)
df_memory_mfa_10  = pd.read_csv('20210514_10_coap_memory_proposta.csv',names=cols_memory,header=None)


#print(df.to_string())
print("\nmemory")
print("\nno auth")
print(df_memory_noauth_10.describe(include='all'))
print("\nauth")
print(df_memory_auth_10.describe(include='all'))
print("\ntime")
print(df_memory_mfa_10.describe(include='all'))
