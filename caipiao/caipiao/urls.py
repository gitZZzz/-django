"""caipiao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.templates/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

"""
这里是一级路由,也就是网页地址栏里输入一个指定的地址,调用对应的二级路由,
url()里第一个参数是正则,只写一个'^'代表在网页上输入'http://127.0.0.1:8000/'
时直接进入到后面第二个参数的二级路由内,include里的参数是某一个app内的urls文件,
即用户在网页上输入'http://127.0.0.1:8000/'时进入lottery应用内的urls文件内找寻里面的二级路由

"""


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('lottery.urls', namespace='caipiao'))
]
