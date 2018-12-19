
from django.conf.urls import url,include
from . import views
"""
新创建的app目录里是没有这个urls.py文件的,需要手动创建,里面的配置基本与
caipiao目录下的urls.py一致,配置成功后用户在url地址栏里输入http://127.0.0.1:8000/{caipiao里url的地址}/{app里url的地址}
才能调用对应的视图函数,url(r'^caipiao/$', views.index)第一个参数是正则表达式,
第二个参数是一个函数,表示当用户输入这个正则表达式对应的路由时即调用一个指定的视图函数,
由于views.py里使用的类视图,不能直接使用,所以需要在views.Index后面加上.as_view()
代表把这个类当成一个函数来使用
"""


urlpatterns = [

    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^renwenpan/', views.RenWenPan.as_view(), name='renwenpan')
]
