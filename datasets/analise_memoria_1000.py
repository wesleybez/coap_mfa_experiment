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
df_memory_auth_10    = pd.read_csv('20210512_10_coap_memory_autenticated.csv',names=cols_memory,header=None)
df_time_noauth_10  = pd.read_csv('20210512_10_coap_publish_non_auth.csv',names=cols_time,header=None)
df_memory_noauth_10  = pd.read_csv('20210512_10_coap_memory_non_auth.csv',names=cols_memory,header=None)
df_time_mfa_10  = pd.read_csv('20210512_10_coap_publish_proposta.csv',names=cols_time,header=None)
df_memory_mfa_10  = pd.read_csv('20210512_10_coap_memory_proposta.csv',names=cols_memory,header=None)


df_time_auth_100    = pd.read_csv('20210512_100_coap_publish_autenticated.csv',names=cols_time, header=None)
df_memory_auth_100   = pd.read_csv('20210512_100_coap_memory_autenticated.csv',names=cols_memory,header=None)
df_time_noauth_100  = pd.read_csv('20210512_100_coap_publish_non_auth.csv',names=cols_time,header=None)
df_memory_noauth_100  = pd.read_csv('20210512_100_coap_memory_non_auth.csv',names=cols_memory,header=None)
df_time_mfa_100  = pd.read_csv('20210512_100_coap_publish_proposta.csv',names=cols_time,header=None)
df_memory_mfa_100  = pd.read_csv('20210512_100_coap_memory_proposta.csv',names=cols_memory,header=None)



df_time_auth_1000    = pd.read_csv('20210512_1000_coap_publish_autenticated.csv',names=cols_time, header=None)
df_memory_auth_1000    = pd.read_csv('20210512_1000_coap_memory_autenticated.csv',names=cols_memory,header=None)
df_time_noauth_1000  = pd.read_csv('20210512_1000_coap_publish_non_auth.csv',names=cols_time,header=None)
df_memory_noauth_1000  = pd.read_csv('20210512_1000_coap_memory_non_auth.csv',names=cols_memory,header=None)
df_time_mfa_1000  = pd.read_csv('20210512_1000_coap_publish_proposta.csv',names=cols_time,header=None)
df_memory_mfa_1000  = pd.read_csv('20210512_1000_coap_memory_proposta.csv',names=cols_memory,header=None)

#print(df.to_string())
print("\nno auth")
print("\nmemory")
print(df_memory_noauth_1000.describe(include='all'))
print("\ntime")
print(df_time_noauth_1000.describe(include='all'))
print("\n\n\n") 
print("\nauth")
print("\nmemory")
print(df_memory_auth_1000.describe(include='all'))
print("\ntime")
print(df_time_auth_1000.describe(include='all'))


#sns.histplot(df_time_noauth_100,row="nro",col="publish",kde=True)
#plt.show()

#fig = df_time_auth_1000.plot.bar(x="nro",y=["connection","publish"])#, y=["P25th", "Median", "P75th"] , subplots=True

#fig.show()
#df_memory_auth_1000.plot()
#plt.show()
#df_time_auth_1000.plot(x="Rank", y=["P25th", "Median", "P75th"])