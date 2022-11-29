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

df_time_10    = pd.read_csv('20210514_10_coap_publish_proposta.csv',names=cols_time, header=None)
df_time_100  = pd.read_csv('20210514_100_coap_publish_proposta.csv',names=cols_time,header=None)
df_time_200  = pd.read_csv('20210514_200_coap_publish_proposta.csv',names=cols_time,header=None)

print("\ntime")
print("\n10")
print(df_time_10[['connection','publish']].describe(include='all'))
print("\nauth")
print(df_time_100[['connection','publish']].describe(include='all'))
print("\nmfa")
print(df_time_200[['connection','publish']].describe(include='all'))