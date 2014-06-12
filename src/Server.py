#coding:utf-8

from hao.thrift import Hello
from hao.thrift.ttypes import *

from thrift.transport import TSocket
from thrift.protocol import TCompactProtocol 
from thrift.server import TServer 

class HelloHandler(Hello.Iface): 
    def echoDemo(self, demo): 
        return "Demo: name=" + demo.name + "  age=" + str(demo.age);
          
    def echoHello(self, param): 
        result = "你发的字符串是：" + param 
        return result 
    
handler = HelloHandler() 
processor = Hello.Processor(handler)     
  
socket = TSocket.TServerSocket(host="localhost", port=9000) 
factory = TTransport.TFramedTransportFactory() 
protocol = TCompactProtocol.TCompactProtocolFactory() 

#不支持windows
#server = TServer.TForkingServer(processor, socket, factory, protocol) 
server = TServer.TThreadPoolServer(processor, socket, factory, protocol)
  
print "python start server port: 9000"
server.serve()