import os, re, pymysql

from structure.tools.structure.tools import initer

from static.zshell_package.template_data import template,get_template
# from Auto_work_helper.structure.tools.structure.tools import initer

def init_struct(project):
    cf = initer(
        PROJECT=project,
        APPNAME=['qq1', 'qq2', 'qq3'],
        RUNSERVER=False,
        CONFIGURATION='',
        PUSHGIT=False,
    )
    print('开始获取路径')
    DATABASENAME = cf.DATABASENAME
    PROJECT = cf.PROJECT
    APPNAME = cf.APPNAME
    RUNSERVER = cf.RUNSERVER
    CONFIGURATION = cf.CONFIGURATION
    BASE_DIR = cf.BASE_DIRS
    SETTINGS = cf.SETTINGS
    VIEWS = cf.VIEWS
    URLS = cf.URLS
    os.chdir(BASE_DIR)

    print('路径获取完成...')

    if not os.path.exists(PROJECT):
        print('开始初始化配置...')

        print('开始设置数据库...')
        cf.setting_database()
        print('数据库设置完成...')

        print('开始修改主模块setting和urls...')
        cf.set_init_info()
        print('修改主模块setting和urls完成..')

        print('开始创建主模块必要文件...')
        cf.create_main_dirs(PROJECT)
        print('主模块必要文件创建完成...')

        print('开始写入模板信息...')
        cf.write_base_info_in_files()
        print('写入模板信息完成...')


        print('初始化配置完成...')
    # app配置
    if APPNAME:
        print('开始初始化分应用...')
        for appname in APPNAME:
            if os.path.exists(BASE_DIR + '/' + PROJECT + '/' + appname):
                pass
            else:
                os.chdir(BASE_DIR + '/' + PROJECT)
                os.system('python3 manage.py startapp %s' % appname)
                cf.main_settings_change(r"'django.contrib.staticfiles',",
                                        "'django.contrib.staticfiles',\n    '%s'," % appname)
                cf.setting_app_info(appname)
                cf.main_urls_change(r"path('admin/', admin.site.urls),",
                                    "    path('admin/', admin.site.urls),\n      path('/%s',include(%s.urls))," % (
                                        appname, appname))
                template_of_app = get_template(appname, BASE_DIR)
                APPURLS = BASE_DIR + '/' + PROJECT + '/' + appname + '/' + 'urls.py'
                APPVIEWS = BASE_DIR + '/' + PROJECT + '/' + appname + '/' + 'views.py'
                APPMODELS = BASE_DIR + '/' + PROJECT + '/' + appname + '/' + 'models.py'
                APPTEMPLATES = BASE_DIR + '/' + PROJECT + '/' + appname + '/' + 'templates'
                APPSTATIC = BASE_DIR + '/' + PROJECT + '/' + appname + '/' + 'static'
                APPCSS = APPSTATIC + '/' + appname + '/' + 'css' + '/' + appname + '.css'
                APPTOOLS = BASE_DIR + '/' + PROJECT + '/' + appname + '/' + 'tools'
                APPSTART = BASE_DIR + '/' + PROJECT + '/' + appname + '/' + 'templates' + '/' + appname + '/' + 'start.html'
                cf.write_base_info_in_afile(file=APPURLS, template=template['app_urls'])
                cf.write_base_info_in_afile(file=APPVIEWS, template=template_of_app['app_views'])
                cf.write_base_info_in_afile(file=APPSTART, template=template_of_app['app_start_html'])

        print('初始化分应用完成...')



    else:
        print('APP is error or no exist')

    if CONFIGURATION:
        pass

    if RUNSERVER:
        print('开始以调试方式启动...')

        os.system('python3 %s/manage.py runserver' % PROJECT)
        print('以调试方式启动完成...')


if __name__ == '__main__':
    init_struct('nihao')