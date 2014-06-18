namespace java com.hao.demo.thrift
namespace py hao.thrift

/*
定义一个结构，相当于java的javabean
*/
struct Demo{
    1:string name,
    2:i32 age
}


/*
定义一个类
*/
service Hello{
    string echoDemo(1:Demo demo),
    
    string echoHello(1:string str),
    
    void uploadFile(1:binary binaryData, 2:string filePath, 3:i16 flag)
}
