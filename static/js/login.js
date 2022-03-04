$(document).ready(function(){
   
  /** username not null*/
  $("#id_username").focus(function(){
    $("#helptextUser").fadeOut("slow");
  });
  $("#id_username").blur(function(){
    var username = $("#id_username").val();
    if(username == ""){
        $("#helptextUser").fadeIn("slow");
        console.log("--",username)
    }  
  });

  /** email not null*/
 $("#id_email").focus(function(){
    $("#helptextEmail").fadeOut("slow");
    $("#helptextEmail2").fadeOut("slow");
  });
  $("#id_email").blur(function(){
    var email = $("#id_email").val();
    if(email == ""){
        $("#helptextEmail").fadeIn("slow");
       
    }  
    var reg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])/;//邮箱格式包括_-两个符号
		if(!reg.test(email)){
            $("#helptextEmail2").fadeIn("slow");
		}else{
            $("#helptextEmail2").fadeOut("slow"); 
        }
  });

 /** password not null*/
 $("#id_password1").focus(function(){
    $("#helptextPassword1").fadeOut("slow");
  });
  $("#id_password1").blur(function(){
    var password1 = $("#id_password1").val();
    if(password1 == "" ){
        $("#helptextPassword1").fadeIn("slow");
        
    }

  });

  /** confirmPassword not null*/
 $("#id_password2").focus(function(){
    $("#helptextPassword2").fadeOut("slow");
    if(password1 = password2)  {
        $("#helptextPassword2").fadeOut("slow");
        $("#helptextPassword3").fadeIn("slow");
    }
    
  });
  $("#id_password2").blur(function(){
    var password1 = $("#id_password1").val();
    var password2 = $("#id_password2").val();
    if(password2 == ""){
        $("#helptextPassword2").fadeIn("slow");
    }else if(password1 != password2)  {
        $("#helptextPassword3").fadeIn("slow");
    }else if(password1 = password2){
        $("#helptextPassword2").fadeOut("slow");
        $("#helptextPassword3").fadeOut("fast");
    }
  });




});
