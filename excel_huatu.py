#-*- coding: utf-8 -*-

from xlrd import open_workbook
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from xlrd import open_workbook
import xlrd
from matplotlib.font_manager import FontProperties  
import configparser

cp = configparser.SafeConfigParser()
cp.read('app.conf')

zhfont1 = FontProperties(fname='C:\\Windows\\Fonts\\simkai.ttf')
x_data1=[]
y_data1=[]
x_volte=[]
temp=[]

for files in cp.sections():
    wb = open_workbook('C:\\Users\\liyi\\Desktop\\'+files)

    for s in wb.sheets():
        print ("Sheet:",s.name)
        for row in range(s.nrows):
            print ('the row is:'),row
            values = []
            for col in range(s.ncols):
                values.append(s.cell(row,col).value)
            print (values)
            x_data1.append(values[0])
            try:
                y_data1.append(float(values[1]))
            except:
                y_data1.append(values[1])
            # print (y_data1)

        tick_spacing = 1
        # tick_spacing = 1
        fig, ax = plt.subplots(1,1)
        fig.autofmt_xdate(rotation = 45)
        ax.plot(x_data1, y_data1, 'bo-',label=u"Phase curve",linewidth=1)
        # plt.axis('auto')
        # ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing)) 
        plt.legend()

        plt.title(s.name,fontproperties=zhfont1)
        plt.xlabel(u"时间",fontproperties=zhfont1)
        plt.ylabel(s.name,fontproperties=zhfont1)
        plt.grid()
        plt.savefig(s.name + ".jpg")
        plt.show()
        plt.close()
        x_data1=[]  
        y_data1=[]
        
        print ('over!')