# -*- coding: utf-8 -*-
#测试

import os,re,pymysql
from zshell_package.shellTools import modification,main_urls_change,configuration,setting_app_info


DATABASENAME = configuration.DATABASENAME
PROJECT = configuration.PROJECT
APPNAME = configuration.APPNAME
RUNSERVER = configuration.RUNSERVER


# 不需要输入的
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SETTINGS = BASE_DIR+'/'+PROJECT+'/'+PROJECT+'/'+'settings.py'
VIEWS = BASE_DIR+'/'+PROJECT+'/'+PROJECT+'/'+'views.py'
URLS = BASE_DIR+'/'+PROJECT+'/'+PROJECT+'/'+'urls.py'

import mpld3
"""
demo08_polar.py 极坐标系
"""
import matplotlib.pyplot as mp
import numpy as np

mp.figure("Polar", facecolor='lightgray')
mp.gca(projection='polar')
mp.title('Porlar', fontsize=20)
mp.xlabel(r'$\theta$', fontsize=14)
mp.ylabel(r'$\rho$', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 准备数据
t = np.linspace(0, 4 * np.pi, 1000)
r = 0.8 * t
mp.plot(t, r)

mp.savefig(BASE_DIR+'/'+PROJECT+'/static/pp.png')
mp.show()
# html = mpld3.fig_to_html(fig)
# plt.close()
# return html