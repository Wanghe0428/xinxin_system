var userName;
var ws;

$(function() {
	userName =localStorage.getItem("user_name");
	if(window.WebSocket) {
		if(ws == null) { //创建新的连接
			ws = new WebSocket("ws://127.0.0.1:9000");
		} else {
			if(ws.readyState == 3) { //若连接断开，则重新创建连接
				ws = new WebSocket("ws://127.0.0.1:9000");
			}
		}
		ws.onopen = function() {
			//ws.send(userName); //连接后将用户名传送给服务器
		}
		ws.onmessage = function(e) {
			appendMsg(e.data);
		}
	}
	
	function appendMsg(sdata){
		var data = JSON.parse(sdata);
        var box = $(".chatbox ul");
        var content = '<div class="layim-chat-user">\
            <cite>'+data.userName+'</cite>\
        </div>\
        <div class="layim-chat-text">'+data.msg+'</div>';
        if(userName==data.userName){
            box.append("<li class='layim-chat-mine'>"+content+"</li>")
        }else{
            box.append("<li>"+content+"</li>")
        }
        $(".chatbox")[0].scrollTop =  $(".chatbox")[0].scrollHeight;
    }
	

	 $("#inputcontent").keyup(function (e) {  //方式1.按回车
	        if (event.keyCode == 13) {
	            sendMsg();
	        }
	    });
	 $("#sendMsg").click(sendMsg);          //方式2.点击发送按钮
	 
	 function sendMsg(){
	        var content = $("#inputcontent").val();
	        if(content.trim()){
	            $("#inputcontent").val("");
	            var data = {
	                    userName:userName,
	                    msg:content
	             };
	            var sdata=JSON.stringify(data);
	            ws.send(sdata); //将信息框的内容发给服务器
	        }
	 }

});