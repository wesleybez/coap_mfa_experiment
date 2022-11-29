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

df_time_auth_10    = pd.read_csv('20210512_10_coap_publish_autenticated.csv',names=cols_time, header=None)
df_time_noauth_10  = pd.read_csv('20210512_10_coap_publish_non_auth.csv',names=cols_time,header=None)
df_time_mfa_10  = pd.read_csv('20210513_10_coap_publish_proposta.csv',names=cols_time,header=None)

print("\ntime")
print("\nno auth")
print(df_time_noauth_10.describe(include='all'))
print("\nauth")
print(df_time_auth_10.describe(include='all'))
print("\nmfa")
print(df_time_mfa_10.describe(include='all'))