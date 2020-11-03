from django.shortcuts import render
from .tools.structure.shell import init_struct
# Create your views here.
def appstart_view(request):
    if request.method == 'GET':
        return render(request,'structure/start.html',locals())
    elif request.method == 'POST':
        test1 = request.POST.get('test1')
        print('初始化开始')
        init_struct(test1)
        print('初始化完成')
        return render(request,'structure/start.html',locals())



