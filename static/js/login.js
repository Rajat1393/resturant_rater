$(document).ready(function() {
    $("#helptextUser").hide()
    $("#helptextEmail").hide()
    $("#helptextEmail2").hide()
    $("#helptextPassword1").hide()
    $("#helptextPassword2").hide()
    $("#helptextPassword3").hide()
        /** username not null*/
    $("#id_username").focus(function() {
        $("#helptextUser").hide();
    });
    $("#id_username").blur(function() {
        var username = $("#id_username").val();
        if (username == "") {
            $("#helptextUser").show();
        }
    });

    /** email not null*/
    $("#id_email").focus(function() {
        $("#helptextEmail").hide();
        $("#helptextEmail2").hide();
    });
    $("#id_email").blur(function() {
        var email = $("#id_email").val();
        if (email == "") {
            $("#helptextEmail").show();

        }
        var reg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])/; //邮箱格式包括_-两个符号
        if (!reg.test(email)) {
            $("#helptextEmail2").show();
        } else {
            $("#helptextEmail2").hide();
        }
    });

    /** password not null*/
    $("#id_password1").focus(function() {
        $("#helptextPassword1").hide();
    });
    $("#id_password1").blur(function() {
        var password1 = $("#id_password1").val();
        if (password1 == "") {
            $("#helptextPassword1").show();

        }

    });

    /** confirmPassword not null*/
    $("#id_password2").focus(function() {
        $("#helptextPassword2").hide();
        if (password1 = password2) {
            $("#helptextPassword2").hide();
            $("#helptextPassword3").show();
        }

    });
    $("#id_password2").blur(function() {
        var password1 = $("#id_password1").val();
        var password2 = $("#id_password2").val();
        if (password2 == "") {
            $("#helptextPassword2").show();
        } else if (password1 != password2) {
            $("#helptextPassword3").show();
        } else if (password1 = password2) {
            $("#helptextPassword2").hide();
            $("#helptextPassword3").hide();
        }
    });
});