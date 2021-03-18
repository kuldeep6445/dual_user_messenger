var input = document.getElementById("main_input");

const ws = new WebSocket("ws://13.232.23.83:8080");
ws.addEventListener("open",()=>{
	console.log("we are connected");
    ws.send("2");
});

ws.addEventListener("message",data=>{
    console.log(`server has sent us ${data.data}`);
    record_message(data.data);
});

function record_message(data){
    var mess = JSON.parse(data);
    if(mess.sent_data=="co-nn-ect-ed"){
        const stat = document.getElementById("nav_status");
        stat.innerText="   connected"; 
        return;
    }
    var para = document.createElement("p");
    para.className = "client_class";
    para.innerText = mess.date_time+" ~>"+mess.sent_data+"\n";
    document.getElementById("room1").appendChild(para);
}


input.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
   event.preventDefault();
   read_now(input.value);
  }
});

function submit_button(){
	read_now(input.value);
}

function read_now(data){
    console.log(`sending data : ${data}`);
	const abc = JSON.stringify({
		user : "admin",
		date_time : get_time(),
		sent_data : data
	});
	ws.send(abc);
    add_element(data);
	console.log(abc);
}

function check(i) {
    if (i < 10) {i = "0" + i};  
    return i;
  }

function get_time(){
	var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = check(m);
    s = check(s);
    date_text = today.getDate()+"-"+ today.getMonth()+"-"+today.getFullYear()+ "|"+h + ":" + m + ":" + s;
    return date_text;
}

function add_element(data){
    date_text = get_time();
    var text = date_text + " ~>" +data + '\n';
    var para = document.createElement("p");
    para.innerText = text;
    para.style = "display:inline";
    document.getElementById("room1").appendChild(para);
}