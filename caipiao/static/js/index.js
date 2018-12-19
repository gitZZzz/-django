$(document).ready(function () {
    // 点击某个按钮,给当前这个按钮添加一个active样式显示按下状态
    $('#sx button').click(function () {
        if ($(this).hasClass('active1')) {
            // $(this).css('background-color', '#fff');
            // $(this).removeClass('active1');
        }
        else {
            // $(this).css('background-color', '#888');
            $('#sx button').removeClass('active1');
            $(this).addClass('active1');
            // 获取选中的生肖标签的文本内容
            var shengxiao = $(this).text();
            // 发送get请求到renwenpan/路由,第2个参数是个字典类型,后端通过key获取值,第三个是
            // 一个函数,function(data)括号内的data是后端返回的json数据,
            // 函数内可以处理这个json数据
            $.get('renwenpan/', {'shengxiao': shengxiao}, function (data) {
                // 把选择
                for (var i=0;i<=11;i++) {
                    // console.log(data[''][i][1]);
                    $('#sx'+(i+1)+' tr:nth-child(2)>td:nth-child(2)').html(data['shengxiao'][i][0]);
                    $('#sx'+(i+1)+' tr:nth-child(2)>td:nth-child(3)').html(data['shengxiao'][i][1]);
                }


            })
        }

    })


});