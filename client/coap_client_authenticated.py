#https://github.com/Tanganelli/CoAPthon
from coapthon.client.helperclient import HelperClient
import threading
import time
import logging
import configparser

import json

from common.user import CoapUser
from common.device import CoapDevice
from common import mem_util

from coapthon.messages.response import Response

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

config = configparser.ConfigParser()
config.read('../config.ini')
LOOP_NUMBER = config.getint('geral','instance_number')
FATOR_MULT = config.getint('geral','mult_factor')
HOST = config.get('geral','host')
PORT = config.getint('geral','port')
DATASET_DIR = config.get('geral','dataset_dir')

medicoes = open(DATASET_DIR+time.strftime('%Y%m%d')+"_"+str(LOOP_NUMBER)+"_coap_publish_autenticated.csv","w")
memoria = open(DATASET_DIR+time.strftime('%Y%m%d')+"_"+str(LOOP_NUMBER)+"_coap_memory_autenticated.csv","w")



path1 ="basic"
path2 ="sala/teste"
path3 ="jardim/teste"

client = None

auth_code = ""

def cb_post_login(response):
    logger.debug ("\n\n\n\ndentro do callback do post do login")
    logger.debug(response)
    auth_code = response.payload
    print("auth_code:",auth_code)
    #client.stop
def cb_put_data(response):
    logger.debug ("\n\n\n\ndentro do callback do put data")
    print("data response:",response)
    #response.stop()
    #client.stop
    
def autenticar(client):
    #
    # conectar ao servico de autenticacao e obter credencial
    #
    #envio das credenciais
    logger.debug("Conectando no servico de autenticacao")
    usuario = CoapUser("sensor1","senha1")
    response = client.post("login", usuario.toCSV(), cb_post_login, 1)
    if response is not None:
        logger.debug (response.pretty_print())
    #client.stop()
    print("response",response)

def enviar_dados(client,cont):
    logger.debug("Conectando no servico de dados")    
    client.put("basic", "aleatorio_"+str(cont), cb_put_data, 10)
    
def worker(cont):
    t_inicio = time.perf_counter()
    mem_inic = mem_util.getCurrentMemoryUsage()
    #coap client
    client = HelperClient(server=("127.17.0.1", 5683))  
    autenticar(client)
    t_connection = time.perf_counter()
    td_connection = t_connection - t_inicio
    
    enviar_dados(client, cont)     
   # client.put("teste", "aleatorio_"+str(cont), cb_put(), 10)    
    t_publish = time.perf_counter()
    td_publish = t_publish - t_connection
    #
    #time.sleep(1000)
    #client.subscribe("casa/teste_2")
    #response = client.get(path2)
#    print response.pretty_print()
    #time.sleep(1000)
    t_subscribe = time.perf_counter()
    td_subscribe = t_subscribe - t_publish
    #client.stop()
    t_disconnect = time.perf_counter()
    td_disconnect = t_disconnect - t_subscribe
    mem_fim = mem_util.getCurrentMemoryUsage()
    
    medicoes.write(" "+str(cont+1)
                   +","+str(t_inicio*FATOR_MULT)
                   +","+str(td_connection*FATOR_MULT)
                   +","+str(td_publish*FATOR_MULT)
                   +","+str(td_subscribe*FATOR_MULT)
                   +","+str(td_disconnect*FATOR_MULT)
                   +"\n")
    medicoes.flush()
    memoria.write(" "+str(cont+1)
                  +","+str(mem_inic)
                  +","+str(mem_fim)
                  +","+str(mem_fim-mem_inic)+"\n")
    memoria.flush()
#medicoes.write("thread ,inicio ,conexao ,publicacao ,inscricao ,fim [x1000] \n")



clients = list()
for i in range(LOOP_NUMBER):
    c= threading.Thread(target=worker,args=(i,))
    clients.append(c)
    c.start()
    time.sleep(1)
        
time.sleep(5)

medicoes.close()
memoria.close()
#client.subscribe("casa/teste_2")