/**
 * Created by Administrator on 2018/10/31.
 */
function changeFrameHeight(){
    var ifm= document.getElementById("iframepage");
    ifm.height=document.documentElement.clientHeight;

}

window.onresize=function(){
     changeFrameHeight();

}