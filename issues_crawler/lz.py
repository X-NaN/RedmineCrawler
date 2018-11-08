#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/05/07 11:57
# @Author  : Nana Xing
# @Site    : 
# @File    : lz.py
# @Software: PyCharm
#__author__ = 'xu.duan'
# -*- coding: utf-8 -*-

import cairo
import pycha.pie
import pycha.bar
import pycha.scatter
import pycha.stackedbar
import pycha.line
import time
from redminelib import Redmine
import xlwt

# settings redmine,redmine's url :http://python-redmine.readthedocs.org/
def set_Redmine():
    REDMINE_URL = 'http://redmine.meizu.com' #redmine 的地址
    REDMINE_KEY = 'fb88cc2ee088296f1cfeac00846cdac197cba867'#这个是自己redmine的账号
    redmine = Redmine(REDMINE_URL,key=REDMINE_KEY)
    issues = redmine.issue.all(project_id = 'M1809',status_id='*',tracker_id=23)
    return issues

#获取multimode的数据
def hybrid_API_multimode():
    Low = []
    Normal = []
    High =[]
    Urgent =[]
    Immediate = []
    openlist=[]
    colselist =[]
    for i in set_Redmine():
        try:
            if str(i.category) =='hybrid-API-multimode' and str(i.priority) =="Low":
                Low.append(i)
            elif str(i.category) =='hybrid-API-multimode' and str(i.priority) =="Normal":
                Normal.append(i)
            elif str(i.category) =='hybrid-API-multimode' and str(i.priority) =="High":
                High.append(i)
            elif str(i.category) =='hybrid-API-multimode' and str(i.priority) =="Urgent":
                Urgent.append(i)
            elif str(i.category) =='hybrid-API-multimode' and str(i.priority) =="Immediate":
                Immediate.append(i)
            if str(i.category) =='hybrid-API-multimode' and str(i.status) == "New":
                openlist.append(i)
            if str(i.category) =='hybrid-API-multimode' and str(i.status) != "New":
                colselist.append(i)
        except Exception as e:
            print (e)
    return len(Low),len(Normal),len(High),len(Urgent),len(Immediate),len(openlist),len(colselist)
#获取search的数据
def hybrid_API_serach():
    Low = []
    Normal = []
    High =[]
    Urgent =[]
    Immediate = []
    openl=[]
    colsel =[]
    for i in set_Redmine():
        try:
            if str(i.category) =='hybrid-API-serach' and str(i.priority) =="Low":
                Low.append(i)
            elif str(i.category) =='hybrid-API-serach' and str(i.priority) =="Normal":
                Normal.append(i)
            elif str(i.category) =='hybrid-API-serach' and str(i.priority) =="High":
                High.append(i)
            elif str(i.category) =='hybrid-API-serach' and str(i.priority) =="Urgent":
                Urgent.append(i)
            elif str(i.category) =='hybrid-API-serach' and str(i.priority) =="Immediate":
                Immediate.append(i)
            if str(i.category) =='hybrid-API-serach' and str(i.status) =="New":
                openl.append(i)
            if str(i.category) =='hybrid-API-serach' and str(i.status) !="New":
                colsel.append(i)
        except Exception as e:
            print (e)
    return len(Low),len(Normal),len(High),len(Urgent),len(Immediate),len(openl),len(colsel)
#获取route&traffic的数据
def hybrid_API_route_traffic():
    Low = []
    Normal = []
    High =[]
    Urgent =[]
    Immediate = []
    openl=[]
    colsel =[]
    for i in set_Redmine():
        try:
            if str(i.category) =='hybrid-API-route&traffic' and str(i.priority) =="Low":
                Low.append(i)
            elif str(i.category) =='hybrid-API-route&traffic' and str(i.priority) =="Normal":
                Normal.append(i)
            elif str(i.category) =='hybrid-API-route&traffic' and str(i.priority) =="High":
                High.append(i)
            elif str(i.category) =='hybrid-API-route&traffic' and str(i.priority) =="Urgent":
                Urgent.append(i)
            elif str(i.category) =='hybrid-API-route&traffic' and str(i.priority) =="Immediate":
                Immediate.append(i)
            if str(i.category) =='hybrid-API-route&traffic' and str(i.status) =="New":
                openl.append(i)
            if str(i.category) =='hybrid-API-route&traffic' and str(i.status) !="New":
                colsel.append(i)
        except Exception as e:
            print (e)
    return len(Low),len(Normal),len(High),len(Urgent),len(Immediate),len(openl),len(colsel)

#设置画布
def set_charvalue():
    width,height=600,600
    surface=cairo.ImageSurface(cairo.FORMAT_ARGB32,width,height)
    return surface

#画饼图
def draw_pie(surface, options, dataSet):
    chart=pycha.pie.PieChart(surface,options)
    chart.addDataset(dataSet)
    chart.render()
    surface.write_to_png('Pie.png')

#垂直直方图
def draw_vertical_bar(surface, options, dataSet):
    chart=pycha.bar.VerticalBarChart(surface,options)
    chart.addDataset(dataSet)
    chart.render()
    surface.write_to_png('vertical_bar.png')

#垂直水平直方图
def draw_horizontal_bar(surface, options, dataSet):
    chart = pycha.bar.HorizontalBarChart(surface,options)
    chart.addDataset(dataSet)
    chart.render()
    surface.write_to_png('horizontal_bar.png')

#线图
def draw_line(surface, options, dataSet):
    chart = pycha.line.LineChart(surface,options)
    chart.addDataset(dataSet)
    chart.render()
    surface.write_to_png('line.png')

#点图
def draw_scatterplot(surface, options, dataSet):
    chart = pycha.scatter.ScatterplotChart(surface,options)
    chart.addDataset(dataSet)
    chart.render()
    surface.write_to_png('scatterplotChart.png')

#垂直块图
def draw_stackedverticalbarChar(surface, options, dataSet):
    chart = pycha.stackedbar.StackedVerticalBarChart(surface,options)
    chart.addDataset(dataSet)
    chart.render()
    surface.write_to_png('stackedVerticalBarChart.png')

#垂直块图2
def draw_stackweekChar(surface, options, dataSet):
    chart = pycha.stackedbar.StackedVerticalBarChart(surface,options)
    chart.addDataset(dataSet)
    chart.render()
    surface.write_to_png('stackweekChar.png')

#水平块图
def draw_stackedhorizontalbarChart(surface, options, dataSet):
    chart = pycha.stackedbar.StackedHorizontalBarChart(surface,options)
    chart.addDataset(dataSet)
    chart.render()
    surface.write_to_png('stackedhorizontalbarChart.png')

def set_style(name,height,bold=False):
  style = xlwt.XFStyle() # 初始化样式

  font = xlwt.Font() # 为样式创建字体
  font.name = name # 'Times New Roman'
  font.bold = bold
  font.color_index = 4
  font.height = height

  # borders= xlwt.Borders()
  # borders.left= 6
  # borders.right= 6
  # borders.top= 6
  # borders.bottom= 6

  style.font = font
  # style.borders = borders

  return style
if __name__ == '__main__':
    '''
    Function:Hybrid-BUG数据分析图
    Input：redmin
    Output: excel+PNG
    '''
    #分布图数据数据来源


    mLow,mNormal,mHigh,mUrgent,mImmediate,mopen,mcolse= hybrid_API_multimode()
    sLow,sNormal,sHigh,sUrgent,sImmediate,sopen,scolse= hybrid_API_serach()
    rLow,rNormal,rHigh,rUrgent,rImmediate,ropen,rcolse= hybrid_API_route_traffic()
    #Hybrid-bug 整体严重情况分布图数据
    totaLow = mLow+sLow+rLow
    totalNormal = mNormal+sNormal+rNormal
    totalHigh = mHigh+sNormal+rHigh
    totalUrgent = mUrgent+sUrgent+rUrgent
    totalImmediate= mImmediate+sImmediate+rNormal
    #Hybrid bug 模块状态统计数据
    mtotal = mopen+mcolse
    stotal = sopen+scolse
    rtotal = ropen+rcolse
    #Hybrid bug weekly状态统计数据
    totalopen = mopen+sopen+ropen
    totalcolse = mcolse+scolse+rcolse
    totalC = totalopen+totalcolse
    print (sopen,scolse)

    #画条形图
    dataSet1=(
             ('open',((0,int("%d"%mopen)),(1,int("%d"%ropen)),(2,int("%d"%sopen)))),
             ('close',((0,int("%d"%mcolse)),(1,int("%d"%rcolse)),(2,int("%d"%scolse)))),

            )

    #图像属性定义
    options1={
                'legend':{'hide':False},
                'title':'Hybrid bug 模块状态统计',
                'titleColor':'#0000ff',
                'titleFont':'字体',
                #'background':{'chartColor': '#ffffff'},
                'axis':{
                    'x': {
                'ticks': [dict(v=0, label='hybrid-API-multimode'),
                          dict(v=1, label='hybrid-API-route&traffic'),
                          dict(v=2, label='hybrid-API-serach'),],
                'label': 'Items',
                'labelColor':'#0000C6'
            },
            'y': {
                'tickCount':8,
                'label': 'status',
                'labelColor':'#0000C6'}
            },
            'background': {
            'chartColor': '#ffffff',     #图表背景色
            'baseColor': '#ffffff',      #边框颜色
            'lineColor': '#E0E0E0'       #横线颜色
        },
            'colorScheme': {
            'name': 'fixed',
            'args': {
                'colors': ['#A42D00', '#227700'], #图表颜色
            },
        },
    }

    #画饼图
    dataSet2=(
             ('Low',((0,int("%d"%totaLow)),(1,int("%d"%totaLow)))),
             ('Normal',((0,int("%d"%totalNormal)),(1,int("%d"%totalNormal)))),
             ('High',((0,int("%d"%totalHigh)),(1,int("%d"%totalHigh)))),
             ('Urgent',((0,int("%d"%totalUrgent)),(1,int("%d"%totalUrgent)))),
             ('Immediate',((0,int("%d"%totalImmediate)),(1,int("%d"%totalImmediate)))),

            )

    #图像属性定义
    options2={
                'legend':{'hide':False},
                'title':'Hybrid bug 模块状态统计',
                'titleColor':'#0000ff',
                'titleFont':'字体',
                #'background':{'chartColor': '#ffffff'},
                'axis':{'labelColor':'#FF0088'},
            'background': {
            'chartColor': '#ffffff',     #图表背景色
            'baseColor': '#ffffff',      #边框颜色
            'lineColor': '#E0E0E0'       #横线颜色
        },
            'colorScheme': {
            'name': 'fixed',
            'args': {
                'colors': ['#FF5511', '#A42D00','#227700','#0066FF','#99FF33'], #图表颜色
            },
        },


    }
    #画week图
    dataSet3=(
             ('open',((0,int("%d"%totalopen)),(1,int("%d"%totalopen)),(2,0))),
             ('close',((0,int("%d"%totalcolse)),(1,int("%d"%totalcolse)),(2,0))),

            )

    #图像属性定义
    LastWeek = float(time.strftime("%W"+'.5'))-1
    ThisWeek = float(time.strftime("%W"+'.5'))
    NextWeek = float(time.strftime("%W"+'.5'))+1

    options3={
                'legend':{'hide':False},
                'title':'Hybrid weekly状态统计',
                'titleColor':'#0000ff',
                'titleFont':'字体',
                #'background':{'chartColor': '#ffffff'},
                'axis':{
                    'x': {
                'ticks': [dict(v=0, label='%s'%LastWeek),
                          dict(v=1, label='%s'%ThisWeek),
                          dict(v=2, label='%s'%NextWeek),],
                'label': 'Items',
                'labelColor':'#0000C6'
            },
            'y': {
                'tickCount':8,
                'label': 'status',
                'labelColor':'#0000C6'}
            },
            'background': {
            'chartColor': '#ffffff',     #图表背景色
            'baseColor': '#ffffff',      #边框颜色
            'lineColor': '#E0E0E0'       #横线颜色
        },
            'colorScheme': {
            'name': 'fixed',
            'args': {
                'colors': ['#A42D00', '#227700'], #图表颜色
            },
        },


    }
    surface = set_charvalue()

    #根据需要调用不同函数画不同形状的图
    draw_pie(surface, options2, dataSet2)
    #draw_vertical_bar(surface, options, dataSet)
    #draw_horizontal_bar(surface, options, dataSet)
    #draw_scatterplot(surface, options, dataSet)
    draw_stackedverticalbarChar(surface, options1, dataSet1)
    #draw_stackweekChar(surface, options3, dataSet3)
    draw_stackedhorizontalbarChart(surface, options3, dataSet3)
    #draw_pie(surface, options, dataSet)
    f = xlwt.Workbook() #创建工作簿
    #创建sheet1
    sheet1 = f.add_sheet(u'整体严重情况分布图',cell_overwrite_ok=True) #创建sheet2
    row0 = [u'优先级&模块','hybrid-API-multimode','hybrid-API-route&traffic',u'hybrid-API-serach',u'总计']
    column0 = ['Low','Normal','High','Urgent','Immediate',]
    #生成第一行
    for i in range(0,len(row0)):
        sheet1.write(0,i,row0[i],set_style('Times New Roman',220,True))
    #生成第一列
    for i in range(0,len(column0)):
        sheet1.write(i+1,0,column0[i],set_style('Times New Roman',220))

    sheet1.write(1,1,mLow),sheet1.write(1,2,rLow),sheet1.write(1,3,sLow),sheet1.write(1,4,totaLow)
    sheet1.write(2,1,mNormal),sheet1.write(2,2,rNormal),sheet1.write(2,3,sNormal),sheet1.write(2,4,totalNormal)
    sheet1.write(3,1,mHigh),sheet1.write(3,2,rHigh),sheet1.write(3,3,sHigh),sheet1.write(3,4,totalHigh)
    sheet1.write(4,1,mUrgent),sheet1.write(4,2,rUrgent),sheet1.write(4,3,sUrgent),sheet1.write(4,4,totalUrgent)
    sheet1.write(5,1,mImmediate),sheet1.write(5,2,rImmediate),sheet1.write(5,3,sImmediate),sheet1.write(5,4,totalImmediate)

    sheet2 = f.add_sheet(u'bug模块状态统计',cell_overwrite_ok=True) #创建sheet2
    row0 = [u'模块&状态','OPEN','CLOSE',u'总计']
    column0 = ['hybrid-API-multimode','hybrid-API-route&traffic','hybrid-API-serach']
    #生成第一行
    for i in range(0,len(row0)):
        sheet2.write(0,i,row0[i],set_style('Times New Roman',220,True))
    #生成第一列
    for i in range(0,len(column0)):
        sheet2.write(i+1,0,column0[i],set_style('Times New Roman',220))
    sheet2.write(1,1,mopen),sheet2.write(1,2,mcolse),sheet2.write(1,3,mtotal)
    sheet2.write(2,1,ropen),sheet2.write(2,2,rcolse),sheet2.write(2,3,rtotal)
    sheet2.write(3,1,sopen),sheet2.write(3,2,scolse),sheet2.write(3,3,stotal)

    sheet3 = f.add_sheet(u'weekly状态统计',cell_overwrite_ok=True) #创建sheet2
    row0 = [u'总量\周','CW%s'%LastWeek,'CW%s'%ThisWeek,'CW%s'%NextWeek]
    column0 = ['OPEN','CLOSE',u'BUG总量']
    #生成第一行
    for i in range(0,len(row0)):
        sheet3.write(0,i,row0[i],set_style('Times New Roman',220,True))
    #生成第一列
    for i in range(0,len(column0)):
        sheet3.write(i+1,0,column0[i],set_style('Times New Roman',220,True))
    sheet3.write(1,1,totalopen),sheet3.write(1,2,totalopen),sheet3.write(1,3,'')
    sheet3.write(2,1,totalcolse),sheet3.write(2,2,totalcolse),sheet3.write(2,3,'')
    sheet3.write(3,1,totalC),sheet3.write(3,2,totalC),sheet3.write(3,3,'')

    #sheet1.write_merge(7,7,2,4,) #合并列单元格
    #sheet1.write_merge(1,2,4,4,) #合并行单元格
    _data =time.strftime("%Y_%m_%d", time.localtime())
    LastWeek1 = float(time.strftime("%W"+'.5'))
    f.save(r'Ninja Project Bug Statistical Analysis Report_CW%s_%s.xls'%(LastWeek,_data))