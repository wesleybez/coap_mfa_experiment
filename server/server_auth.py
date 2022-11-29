#https://github.com/Tanganelli/CoAPthon
from coapthon.server.coap import CoAP
from coapthon.resources.resource import Resource
from server.resource_basic import BasicResource
from server.resource_basic_login import LoginBasicResource

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        self.add_resource('login/', LoginBasicResource())
        self.add_resource('basic/', BasicResource())
def main():
    server = CoAPServer("127.17.0.1", 5683)
    try:
        print("Servidor com autenticacao em espera...")
        server.listen(10)
    except KeyboardInterrupt:
        print ("Server Shutdown")
        server.close()
        print ("Exiting...")

if __name__ == '__main__':
    main()