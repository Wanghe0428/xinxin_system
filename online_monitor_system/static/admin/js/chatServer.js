var ws=require("websocket-server");
var server=ws.createServer();

server.addListener("connection",function(con) {

    var userName;            //初始化玩家昵称
    var isFirstMsg = true;            //判断是否为客户端向服务端发送的第一条消息
    con.addListener("close",function(){
        server.broadcast("[系统消息]："+userName+"离开直播间");
        
    });
    con.addListener("message",function(msg){
        if (isFirstMsg){    //客户端发送过来的第一条消息是用户名
        	userName=msg;
        	var data = {
                    userName:"系统消息",
                    msg:"欢迎" + userName + "加入直播间！"
             };
            //server.broadcast("欢迎" + userName + "加入直播间！当前在线人数为:" + server.manager.length);
        	var sdata=JSON.stringify(data);
        	server.broadcast(sdata);
            isFirstMsg = false;
        } else {
        	server.broadcast(msg);
        }

    });
});

server.listen(9000);
console.log("server is running at port 9000");
