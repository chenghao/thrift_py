#coding:utf-8

from hao.thrift import Hello

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from hao.thrift.ttypes import Demo

try:
    socket = TSocket.TSocket(host="localhost", port=9000)
    transport = TTransport.TFramedTransport(socket)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    
    client = Hello.Client(protocol)
    transport.open()

    # 1
    print client.echoHello("chenghao_py")
    # 2
    demo = Demo("chenghao_py", 25)
    print client.echoDemo(demo)
    # 3
    sourceFilePath = "E:\\logs\\xiaohuoban.log"
    targetFilePath = "xiaohuoban_t1.log"
    bufsize = 1024 * 1024 * 10
    # 以读模式+二进制模式打开文件
    fp = open(sourceFilePath, "rb")
    flag = 0
    try:
        while True:
            filedata = fp.read(bufsize)
            if not filedata:
                break
            client.uploadFile(filedata, targetFilePath, flag)
            flag += 1

        print "成功。"
    finally:
        fp.close()

except Thrift.TException, ex:
    print "%s" % (ex.message)
finally:
    transport.close()
