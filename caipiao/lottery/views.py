from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View


# Create your views here.


# 类视图,restfull风格api,根据请求方法调用类视图内对应的函数,get请求调用get方法
class Index(View):
    def get(self, request):
        """
        render代表渲染一个网页,第一个参数是requests,第二个参数是模板templates里的一个html文件,

        """
        d = {
            'a': '你好',
            'b': '老王'
        }
        return render(request, 'index.html', d)


class RenWenPan(View):
    def get(self, request):
        """
        切换12生肖对应的人文盘信息
        :param request:
        :return:
        """
        # shu = {
        #     '1': [7, '', 31, '', 7, '马', 19, '', '',6,'','30','',8,'羊',18,'','',5,'',29,'',9,'猴',17,'','',4,'',28,'',10,'鸡',16,'','',3,'',27,'',11,'狗',15,'','',2,'',26,'',12,'猪',14,'',''],
        #     '2': [1, '', 25, '', 1, '鼠', 13, '', '',12,'','36','',2,'牛',24,'','',11,'',35,'',3,'虎',23,'','',10,'',34,'',4,'兔',22,'','',9,'',33,'',5,'龙',21,'','',8,'',32,'',6,'蛇',20,'',''],
        # }
        # 获取ajax发送的get请求的参数
        # print(request.GET.get('shengxiao'))

        data_num = {
            '马': 7,
            '羊': 8,
            '猴': 9,
            '鸡': 10,
            '狗': 11,
            '猪': 12,
            '鼠': 1,
            '牛': 2,
            '虎': 3,
            '兔': 4,
            '龙': 5,
            '蛇': 6,
        }

        data_test = {
            7: [7, '马'],
            8: [8, '羊'],
            9: [9, '猴'],
            10: [10, '鸡'],
            11: [11, '狗'],
            12: [12, '猪'],
            1: [1, '鼠'],
            2: [2, '牛'],
            3: [3, '虎'],
            4: [4, '兔'],
            5: [5, '龙'],
            6: [6, '蛇'],
        }
        test_list = [
            [7, '马'],
            [8, '羊'],
            [9, '猴'],
            [10, '鸡'],
            [11, '狗'],
            [12, '猪'],
            [1, '鼠'],
            [2, '牛'],
            [3, '虎'],
            [4, '兔'],
            [5, '龙'],
            [6, '蛇']
        ]
        data = {
            'shengxiao': []
        }
        sx = data_num[request.GET.get('shengxiao')]
        print(sx)
        if sx <= 6:
            first = sx + 6
            for k, v in data_num.items():
                if v == first:
                    for i in range(v, 13):
                        data['shengxiao'].append(data_test[i])
                        print(i)
                    for j in range(1,v):
                        print(j)
                        data['shengxiao'].append(data_test[j])

        elif sx > 6:
            first = sx - 6
            for k, v in data_num.items():
                if v == first:
                    for i in range(v, 13):
                        data['shengxiao'].append(data_test[i])
                        print(i)
                    for j in range(1, v):
                        print(j)
                        data['shengxiao'].append(data_test[j])

        print(data)

        # JsonResponse返回json数据,第一个参数必须是一个字典
        # json_dumps_params={'ensure_ascii':False}可以保证传过去的json数据中的中文字符正常显示
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


class Spider(View):
    """
    渲染完页面后执行ajax请求,调用爬虫数据更新彩票开奖信息
    """

    def get(self, request):
        pass


class AjaxGetData(View):
    """
    更新完彩票信息后执行ajax请求,从数据库从把对应信息取出来返回给前端页面
    """

    def get(self, requests):
        pass
