

function inputNull(elem){
    return $.trim( $(elem).val() ) == "";
}

$('#submit').bind('click', function(){
    if(inputNull("#code")){
        alert("邀请码不为空");
    }
    return false;
});
