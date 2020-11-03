import re,os,pymysql
import static.zshell_package.template_data as zt

# ['user','order','waybill']

class initer:
    def __init__(self,PROJECT='default',APPNAME='',RUNSERVER=False,PUSHGIT=False,CONFIGURATION=''):
        # 调整参数区域
        # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        # self.BASE_DIRS = os.path.dirname(os.path.abspath(__file__))
        self.BASE_DIRS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
        BASE_DIR = self.BASE_DIRS



        self.DATABASENAME = PROJECT#数据库名称
        self.PROJECT = PROJECT#项目名称
        self.APPNAME = APPNAME#添加模块名称
        self.RUNSERVER = RUNSERVER#是否运行服务器
        self.PUSHGIT = PUSHGIT #是否建立git仓库
        self.CONFIGURATION = CONFIGURATION#配置网页
        self.SETTINGS = BASE_DIR+'/'+PROJECT+'/'+PROJECT+'/'+'settings.py'
        self.VIEWS = BASE_DIR+'/'+PROJECT+'/'+PROJECT+'/'+'views.py'
        self.URLS = BASE_DIR+'/'+PROJECT+'/'+PROJECT+'/'+'urls.py'
        self.STATIC = BASE_DIR+'/'+PROJECT+'/'+'static'
        self.TEMPLATES = BASE_DIR+'/'+PROJECT+'/'+'templates'
        self.MAIN_START_HTML = PROJECT + '/' + 'templates' + '/' + 'start' + '.html'


    def main_settings_change(self,pattern,repl):
        with open(self.SETTINGS,'r') as file_read:
            outcome = file_read.read(4096)
            result = re.sub(pattern,repl,outcome,1)
        with open(self.SETTINGS,'w') as file_write:
            file_write.write(result)

    def main_urls_change(self,pattern,repl):
        with open(self.URLS,'r') as file_read:
            outcome = file_read.read(4096)
            result = re.sub(pattern,repl,outcome,1)
        with open(self.URLS,'w') as file_write:
            file_write.write(result)


    def create_main_dirs(self,PROJECT):
        os.system('mkdir ' + PROJECT + '/' + 'static')
        os.system('mkdir ' + PROJECT + '/' + 'templates')
        os.system('mkdir ' + PROJECT + '/' + 'static' + '/' + 'js')
        os.system('touch ' + PROJECT + '/' + 'static' + '/' + 'js' + '/' + PROJECT + '.js')
        os.system('mkdir ' + PROJECT + '/' + 'static' + '/' + 'css')
        os.system('touch ' + PROJECT + '/' + 'static' + '/' + 'css' + '/' + 'style' + '.css')
        os.system('mkdir ' + PROJECT + '/' + 'static' + '/' + 'imgs')
        os.system('touch ' + PROJECT + '/' + 'templates' + '/' + 'start' + '.html')

    def set_init_info(self):
        print('开始创建项目...')
        os.chdir(self.BASE_DIRS)
        os.system('django-admin startproject %s' % self.PROJECT)
        print('创建项目完成...')

        print('开始设置settings参数...')
        self.set_settings()
        self.add_settings_info()
        print('设置settings参数完成...')

        print('开始设置urls参数...')
        self.set_urls()
        print('设置urls参数完成...')

    def set_settings(self):
        self.main_settings_change(r"TIME_ZONE = 'UTC'", "TIME_ZONE = 'Asia/Shanghai'")
        self.main_settings_change(r"LANGUAGE_CODE = 'en-us'", "LANGUAGE_CODE = 'zh-Hans'")
        self.main_settings_change(r"'DIRS': \[\],", "'DIRS': [os.path.join(BASE_DIR,'templates')],")
        self.main_settings_change(r"'django.middleware.csrf.CsrfViewMiddleware',",
                        "#'django.middleware.csrf.CsrfViewMiddleware',")
        self.main_settings_change(r"'django.db.backends.sqlite3'", "'django.db.backends.mysql'")
        self.main_settings_change(r"'NAME': os.path.join\(BASE_DIR, 'db.sqlite3'\),",
                                "'NAME': '%s',\n        'USER':'root',\n        'PASSWORD':'123456',\n        'HOST':'127.0.0.1',\n        'POST':'3306'" % self.DATABASENAME)

    def set_urls(self):
        self.main_urls_change(r"path\('admin/', admin.site.urls\),",
                            "    path('admin/', admin.site.urls),\n      path('',views.start),")
        self.main_urls_change(r"from django.urls import path",
                            "from django.urls import path\nfrom . import views")
        self.main_urls_change(r"from django.urls import path",
                            "from django.urls import path\nfrom django.urls import include")





    def setting_app_info(self,appname):

        APP_urls =appname + '/' + 'urls.py'
        APP_templates = appname + '/' + 'templates'
        APP_starthtml = appname + '/' + 'templates' + '/' + appname+'/'+'start.html'
        APP_toolsdir = appname + '/' + 'tools' + '/' + appname

        os.system('touch ' + APP_urls)
        os.system('mkdir ' + APP_templates)
        os.system('mkdir ' + APP_templates + '/' + appname)
        os.system('touch ' + APP_starthtml )
        os.system('mkdir ' + appname + '/' + 'tools')
        os.system('mkdir ' + APP_toolsdir )
        os.system('touch ' + APP_toolsdir +'/'+'tools.py')
        os.system('touch ' + APP_toolsdir +'/'+'tools_accession.py')
        os.system('touch ' + APP_toolsdir +'/'+'tools_test.py')


        self.main_urls_change(r"path\('admin/', admin.site.urls\),",
                            "path('admin/', admin.site.urls),\n        path('%s/',include('%s.urls')),"%(appname,appname))

    def setting_database(self):
        db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', charset='utf8')
        cur = db.cursor()
        try:
            cur.execute(f'CREATE DATABASE %s character set utf8mb4;' % self.DATABASENAME)
            db.commit()
        except Exception as e:
            db.rollback()  # 如果提交异常则回到提交前的状态
            print(e)
        cur.close()
        db.close()

    def add_settings_info(self):
        with open(self.SETTINGS, 'a') as file_add:
            file_add.write("STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)")

    def write_base_info_in_afile(self,file='', template=''''''):
        with open(file, 'w') as file_write:
            file_write.write(template)

    def write_base_info_in_files(self):
        print('开始导入jQuery...')
        self.import_JQuery()
        print('导入jQuery完成...')

        print('开始写入模板文件...')
        self.write_base_info_in_afile(file=self.VIEWS, template=zt.template['main_views'])
        self.write_base_info_in_afile(file=self.MAIN_START_HTML, template=zt.template['main_start_html'])
        print('写入模板文件完成...')

    def import_JQuery(self):
        JQUERY = self.BASE_DIRS + '/Auto_work_helper/static/zshell_package/jquery.min.js'
        with open(JQUERY, 'r') as r:
            with open(self.STATIC + '/' + 'js'+'/' + 'jquery.min.js','w') as w:
                for item in r:
                    w.write(item)
