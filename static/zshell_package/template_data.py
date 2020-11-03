
def get_template(appname,BASE_DIR):
    APPNAME= appname
    BASE_DIR = BASE_DIR
    app_views = f"""
from django.shortcuts import render
# Create your views here.
def appstart_view(request):
    if request.method == 'GET':
        return render(request,'{APPNAME}/start.html',locals())
    elif request.method == 'POST':
        test1 = request.POST.get('test1')
        return render(request,'{APPNAME}/start.html',locals())
"""

    app_start_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{APPNAME}测试页</title>
    <link rel="stylesheet" href="../../static/{APPNAME}/css/{APPNAME}.css">
</head>
<body>
<form action="/{APPNAME}/appstart" method="post">
    <p>
        标题：<input type="text"name="test1">
        <input type="submit" value="保存">
    </p>
    <textarea name="content" id="50" cols="30" rows="10"></textarea>
    
</form>
<div>"""+"""
    {{ test1 }}
    {{ content }}
    """+f"""
</div>
<script src="../../static/{APPNAME}/js/jquery.min.js"></script>
<script src="../../static/{APPNAME}/js/{APPNAME}.js"></script>
</body>
</html>

"""
    return {'app_views':app_views,'app_start_html':app_start_html}


template={
    'main_views':
"""
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def start(request):
    if request.method =='GET':

        return render(request,'start.html',locals())
    if request.method =='POST':
        text = request.POST.get('text')

        return render(request,'start.html',locals())
    
    
""",

    'main_start_html':
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Start</title>
</head>
<body>
<h1></h1>
</body>
</html>
""",


    'app_urls':
"""
from django.urls import path
from . import views

urlpatterns = [

    path('appstart',views.appstart_view),
]
""",
'app_start_css':
"""
p{
    background-color: red;

}
"""


}




