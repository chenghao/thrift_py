#coding:utf-8

from hao.thrift import Hello

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from hao.thrift.ttypes import Demo

try:
    socket = TSocket.TSocket(host="localhost",port=9000)
    transport = TTransport.TFramedTransport(socket)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    
    client = Hello.Client(protocol)
    transport.open()
    
    print client.echoHello("chenghao_py")
    
    demo = Demo("chenghao_py", 25)
    print client.echoDemo(demo)
    
except Thrift.TException, ex:
    print "%s" % (ex.message)
finally:
    transport.close()
