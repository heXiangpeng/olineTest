/**
 * Created by guodandan on 2016/3/25.
 */
$(function () {
    //测试数据
  //  $("#idcard").val("370682199006180834");

   $.cookie('sessionUser',null);


    //判断是否退出链接
    var logout=getlogout();
    if(logout=="logout"){
        $.removeCookie("sessionUser",{});//清理cookie
    }else{
        //记住我
        var cookieCur=eval("("+$.cookie('sessionUser')+")")//获取cookie
        if(cookieCur!=null&&cookieCur!=undefined){
            if(cookieCur.remember){
                $("#idcard").val(cookieCur.account);
                $("#password").val("");
                $("#isRemember").attr("checked",true);
            }
        }
    }

    //登录
    $("#submit_btn").on("click", function () {
      //  $("#submit_btn").attr("disabled", true);
    //    var jsonData = {account: $("#idcard").val(), password: $("#password").val(),isRemember:$("#isRemember").is(":checked")};
        $.ajax({
            type: "POST",
            url:"/userlogin",
            data: "idcard="+$("#idcard").val()+"&psw="+$("#password").val(),
            dataType: "json",
            success: function (data) {

                if (data.staut==1){
                     layer.msg("用户名密码错误！");

                }else if (data.staut==0){
                     $.cookie('sessionUser',JSON.stringify(data),{expires:guodandan.cookieDate()});
                    if(data.actstatus=="999999"){
                      window.location.href = "/admin";
                    }else{
                      window.location.href = "/indexexaminee";
                    }

                }
              
            
                       
                        // if(data.data.type=="admin"){
                        //     window.location.href = global_RootPath+"/index_admin.html";
                        // }else{
                        //     window.location.href = global_RootPath+"/index_examinee.html";
                        // }


                 
                //提示错误-清空输入框
                $("#idcard").val("");
                $("#password").val("");
            }
        });
    });
})
