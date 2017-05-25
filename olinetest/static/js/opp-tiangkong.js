/**
 * Created by 朝阳 on 2016/4/6.
 */
var examlib = {};
$(function () {
    $("#btn_save").on("click", function () {
       // var id = $("#singleId").val();
        var title = $.trim($("#title").val());
     //   var options = "##A." + $.trim($("#option_A").val()) + "##B." + $.trim($("#option_B").val()) + "##C." + $.trim($("#option_C").val()) + "##D." + $.trim($("#option_D").val());
        var answer = $.trim($("#answer").val());
        var type = "tiankong";

        if (title == "") {
            guodandan.failAlert('题目不能为空', function () {
                $("#title").focus();
            });
            return;
        }

        if (answer == "") {
            guodandan.failAlert('正确答案不能为空', function () {
                $("#answer").val("");
                $("#answer").focus();
            });
            return;
        }

        $.ajax({
            type: "POST",
            url:"/examinee/tiankongadd",
            data: "title="+title+"&answer="+answer+"&Type="+type,
            dataType: "json",
            success: function (data) {

                if(data.staut==0){
                    guodandan.sucessAlert("保存成功",function(){
                        $("#btn_save").attr("disabled", true);
                         $("#answer").val("");
                         $("#title").val("");

                    });
                }else{
                     guodandan.failAlert("保存失败",function(){

                     });

                }


            }
        });

    })
    //取消按钮-点击事件
    $("#btn_cancel").on("click", function () {
        examlib._btn_cancel();
    });
    //点击新增事件
    $("#addexamlibbtn").on("click", function () {
        $("#show_examlib_tiankong").hide();
        $("#add_examlib_tiankong").show();
        $("#list_examlib_tiankong").hide();
    })
    //点击返回按钮--返回列表需要异步刷新列表
    $("#addexamlibbtnRe").on("click", function () {
        $("#show_examlib_tiankong").hide();
        $("#add_examlib_tiankong").hide();
        $("#list_examlib_tiankong").show();
        examlib._clearDate();
        examlib._btn_cancel();
        examlib.clearTable();
    })
})
//清理列表，重新加载列表
examlib.clearTable = function () {
    if ($('#examlib_datatable').hasClass('dataTable')) {
        dttable = $('#examlib_datatable').dataTable();
        dttable.fnClearTable(); //清空一下table
        dttable.fnDestroy(); //还原初始化了的datatable
    }
    examlib._examlib_datatable();
}
examlib._clearDate=function(){
    $("#singleId").val("");
    $("#title").val("");
    $("#answer").val("");
}
//取消按钮
examlib._btn_cancel = function () {
    $("#btn_save").removeAttr("disabled");
}
//单选题列表
$(function () {
    examlib._examlib_datatable();
})
examlib._examlib_datatable = function () {
    $("#examlib_datatable").dataTable({
        "sAjaxSource": global_RootPath+"/examinee/examlib/type/single?typle=tiankong",
        "sAjaxDataProp": "data",
        "aoColumns": [
            {"mDataProp": "answer"},
            {"mDataProp": "title"},
            {"mDataProp": "answer"},
            {"sDefaultContent": ''}
        ],
        "bAutoWidth": true, //自适应宽度
        "sPaginationType": "full_numbers",
        "oLanguage": guodandan.oLanguage,
        "fnRowCallback": function (nRow, aData, iDisplayIndex) {// 当创建了行，但还未绘制到屏幕上的时候调用，通常用于改变行的class风格
            $('td:eq(3)', nRow).html("<div class='btn-group'>" +
                "<a class='btn btn-small dropdown-toggle' data-toggle='dropdown' href='#'>" +
                " 操作" +
                " <span class='caret'></span>" +
                " </a>" +
                "<ul class='dropdown-menu pull-right'>" +
                " <li><a href=\"javascript:examlib._btn_show_examlib('" + aData.id + "')\" ><i class='icon-edit'></i>    查看</a></li>" +
                " <li><a href=\"javascript:examlib._btn_edit_examlib('" + aData.id + "')\" ><i class='icon-edit'></i>    编辑</a></li>" +
                " <li><a href=\"javascript:examlib._btn_del_examlib('" + aData.id + "')\" ><i class='icon-trash'></i>    删除</a></li>" +
                " </ul>" +
                " </div>");
            $('td:eq(0)', nRow).html(iDisplayIndex + 1);
            return nRow;
        }
    });
}
//查看
examlib._btn_show_examlib = function (id) {
    $.ajax({
        type: "GET",
        url: global_RootPath+"/examlib/id?id=" + id,
        dataType: "json",
        success: function (datarc) {
            $("#show_title").text(datarc.title);
            $("#show_answer").text(datarc.answer);
            $("#add_examlib_tiankong").hide();
            $("#list_examlib_tiankong").hide();
            $("#show_examlib_tiankong").show();
        }
    });
}
//编辑
examlib._btn_edit_examlib = function (id) {
    $.ajax({
        type: "GET",
        url: global_RootPath+"/examlib/id?id=" + id,
        dataType: "json",
        success: function (datarc) {
            var options = datarc.options.split("##")
            $("#singleId").val(datarc.id);
            $("#title").val(datarc.title);
            $("#option_A").val(options[1].substring(options[1].indexOf(".") + 1));
            $("#option_B").val(options[2].substring(options[2].indexOf(".") + 1));
            $("#option_C").val(options[3].substring(options[3].indexOf(".") + 1));
            $("#option_D").val(options[4].substring(options[4].indexOf(".") + 1));
            $("#answer").val(datarc.answer);
            $("#add_examlib_tiankong").show();
            $("#list_examlib_tiankong").hide();
            $("#show_examlib_tiankong").hide();
        }
    });
}
//    删除
examlib._btn_del_examlib = function (id) {
        layer.confirm('确定删除?', function () {
            $.ajax({
                type: "GET",
                url: global_RootPath+"/examlib/delete?id" + id,
                dataType: "json",
                success: function (datarc) {
                    examlib.clearTable();
                    layer.msg('删除成功！');
                }
            });
        });

    }
