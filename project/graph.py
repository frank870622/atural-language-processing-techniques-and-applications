# -*- coding: utf-8 -*-
import matplotlib.pyplot as pl
from matplotlib.gridspec import GridSpec
import numpy
from PIL import Image
import requests
from io import BytesIO

pl.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
pl.rcParams['font.serif'] = ['Microsoft JhengHei']


def fig2img(fig):
    """
    @brief Convert a Matplotlib figure to a PIL Image in RGBA format and return it
    @param fig a matplotlib figure
    @return a Python Imaging Library ( PIL ) image
    """
    # put the figure pixmap into a numpy array
    buf = fig2data(fig)
    w, h, d = buf.shape
    return Image.frombytes("RGBA", (w, h), buf.tostring())


def fig2data(fig):
    """
    @brief Convert a Matplotlib figure to a 4D numpy array with RGBA channels and return it
    @param fig a matplotlib figure
    @return a numpy 3D array of RGBA values
    """
    # draw the renderer
    fig.canvas.draw()

    # Get the RGBA buffer from the figure
    w, h = fig.canvas.get_width_height()
    buf = numpy.fromstring(fig.canvas.tostring_argb(), dtype=numpy.uint8)
    buf.shape = (w, h, 4)

    # canvas.tostring_argb give pixmap in ARGB mode. Roll the ALPHA channel to have it in RGBA mode
    buf = numpy.roll(buf, 3, axis=2)
    return buf


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        pl.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                '%d' % int(height),
                ha='center', va='bottom')


def drawing(string):
    if string == "師生數量":
        figure = pl.figure()
        thegrid = GridSpec(1, 1)
        pl.subplot(thegrid[0, 0])
        labels = '學生', '專任教師', '兼任教師'
        value = [21252, 1326, 684]
        width = 0.5
        rects1 = pl.bar(labels, value, width, color='r')
        autolabel(rects1)
        im = fig2img(figure)
        im.show()
        pl.gcf().clear()
        return im
    elif string == "註冊率":
        array = [
             "              大學    碩士    碩專",
             "95學年度     95.64%  96.64%  98.38%",
             "96學年度     95.32%  95.38%  93.65%",
             "97學年度     97.24%  95.57%  93.08%",
             "98學年度     95.98%  96.94%  99.39%",
             "99學年度     96.01%  92.05%  95.23%",
             "100學年度    95.53%  95.59%  88.42%",
             "101學年度    95.72%  95.01%  88.00%",
             "102學年度    96.49%  93.89%  88.63%",
             "103學年度    95.05%  93.96%  87.98%",
             "104學年度    95.22%  92.67%  88.64%",
             "105學年度    95.31%  94.85%  93.11%",
             "106學年度    95.35%  95.32%  94.40%"
        ]
        outputstring = ""
        for each in array:
            outputstring += each + "\n"
        print(outputstring)
        return outputstring
    elif string == "就業比例":
        figure = pl.figure()
        thegrid = GridSpec(2, 2)
        labels = "工作中", "服役中", "在學中", "待業", "其他"

        pl.subplot(thegrid[0, 0], aspect=1)
        value = [23.61, 3.76, 59.66, 5.71, 7.26]
        pl.pie(value, labels=labels, autopct='%1.1f%%', shadow=True)
        pl.title('學士班')

        pl.subplot(thegrid[0, 1], aspect=1)
        value = [71.54, 8.56, 5.67, 10.67, 3.56]
        pl.pie(value, labels=labels, autopct='%1.1f%%', shadow=True)
        pl.title('碩士班')

        pl.subplot(thegrid[1, 0], aspect=1)
        value = [84.49, 8.02, 0.53, 6.95, 0]
        pl.pie(value, labels=labels, autopct='%1.1f%%', shadow=True)
        pl.title('博士班')

        im = fig2img(figure)
        im.show()
        pl.gcf().clear()

        return im
    elif string == "學測分數":
        response = requests.get(
            "https://www.caac.ccu.edu.tw/cacportal/apply_his_report/106/106_sieve_standard/report/pict/004.png")
        im = Image.open(BytesIO(response.content))
        im.show()
        return im
    elif string == "指考分數":
        array = [
            "中國文學系	            412.00",
            "外國語文學系	        497.55",
            "歷史學系	            379.15",
            "台灣文學系	            504.80",
            "數學系	                365.45",
            "物理學系	            429.25",
            "化學系	                428.35",
            "地球科學系	            334.50",
            "光電科學與工程學系	    364.50",
            "機械工程學系	        356.30",
            "化學工程學系	        360.70",
            "材料科學及工程學系	    370.40",
            "資源工程學系	        342.00",
            "土木工程學系	        346.80",
            "水利及海洋工程學系	    440.50",
            "工程科學系	            356.20",
            "系統及船舶機電工程學系	347.80",
            "航空太空工程學系	    355.50",
            "環境工程學系	        345.70",
            "測量及空間資訊學系	    336.60",
            "生物醫學工程學系	    357.10",
            "工業與資訊管理學系	    351.30",
            "交通管理科學系	        339.40",
            "企業管理學系	        238.00",
            "統計學系	            276.55",
            "會計學系	            572.50",
            "醫學系(自費)	        442.90",
            "醫學系(公費)	        423.40",
            "醫學檢驗生物技術學系	420.60",
            "護理學系	            363.33",
            "職能治療學系	        370.70",
            "物理治療學系	        392.18",
            "藥學系	                414.85",
            "政治學系	            422.55",
            "經濟學系	            443.30",
            "法律學系	            399.20",
            "心理學系	            418.05",
            "電機工程學系	        385.50",
            "資訊工程學系	        376.80",
            "建築學系	            431.43",
            "都市計劃學系	        433.00",
            "工業設計學系	        428.05",
            "生命科學系	            451.53",
            "生物科技與產業科學系	447.85",
            "大一全校不分系學士學位學程	382.00"
        ]
        outputstring = ""
        for each in array:
            outputstring += each + "\n"
        print(outputstring)
        return outputstring


drawing("就業比例")
'''
    figure = pl.figure()
    value = [33, 67]
    value2 = [40, 60]
    labels = '教師比例', '學生比例'
    colors = ['lightcoral', 'lightskyblue']

    thegrid = GridSpec(1, 2)
    pl.subplot(thegrid[0, 0], aspect=1)
    pl.pie(value, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
    pl.title('中葉大學')

    pl.subplot(thegrid[0, 1], aspect=1)
    pl.pie(value2, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
    pl.title('小葉大學')

    im = fig2img(figure)
    im.show()
    pl.gcf().clear()
'''

'''
NCKU
師生數量:
    學生:	21,252人(2017年03月)
    專任教師:	1,326人(2017年03月)
    兼任教師數 :	684(2017年03月)
    註冊率			
                        大學	碩士	 碩專  
            95學年度	95.64%	96.64%	98.38%
            96學年度	95.32%	95.38%	93.65%
            97學年度	97.24%	95.57%	93.08%
            98學年度	95.98%	96.94%	99.39%
            99學年度	96.01%	92.05%	95.23%
            100學年度	95.53%	95.59%	88.42%
            101學年度	95.72%	95.01%	88.00%
            102學年度	96.49%	93.89%	88.63%
            103學年度	95.05%	93.96%	87.98%
            104學年度	95.22%	92.67%	88.64%
            105學年度	95.31%	94.85%	93.11%
            106學年度	95.35%	95.32%	94.40%
    
    目前未就業原因
    103 畢業學制
                        學士班  碩士班  博士班\n
    工作中              23.61   71.54   84.49\n
    服役中              3.76    8.56    0.53\n
    在學中              59.66   5.67    8.02\n
    待業                5.71    10.67   6.95\n
    其他                7.26    3.56    0.00\n
    總和                100.00  100.00  100.00\n
    
    學校可用資金 1,696,974 (千元)
                    
    學測分數:
    https://www.caac.ccu.edu.tw/cacportal/apply_his_report/106/106_sieve_standard/report/pict/004.png
    指考分數    
中國文學系	            412.00
外國語文學系	        497.55
歷史學系	            379.15
台灣文學系	            504.80
數學系	                365.45
物理學系	            429.25
化學系	                428.35
地球科學系	            334.50
光電科學與工程學系	    364.50
機械工程學系	        356.30
化學工程學系	        360.70
材料科學及工程學系	    370.40
資源工程學系	        342.00
土木工程學系	        346.80
水利及海洋工程學系	    440.50
工程科學系	            356.20
系統及船舶機電工程學系	347.80
航空太空工程學系	    355.50
環境工程學系	        345.70
測量及空間資訊學系	    336.60
生物醫學工程學系	    357.10
工業與資訊管理學系	    351.30
交通管理科學系	        339.40
企業管理學系	        238.00
統計學系	            276.55
會計學系	            572.50
醫學系(自費)	        442.90
醫學系(公費)	        423.40
醫學檢驗生物技術學系	420.60
護理學系	            363.33
職能治療學系	        370.70
物理治療學系	        392.18
藥學系	                414.85
政治學系	            422.55
經濟學系	            443.30
法律學系	            399.20
心理學系	            418.05
電機工程學系	        385.50
資訊工程學系	        376.80
建築學系	            431.43
都市計劃學系	        433.00
工業設計學系	        428.05
生命科學系	            451.53
生物科技與產業科學系	447.85
大一全校不分系學士學位學程	382.00



圖片 :師生數量 : https://i.imgur.com/qqqIIVh.png
      就業比例 : https://i.imgur.com/SI7z0YI.jpg (顏色)
    
 
'''

'''
labels = '中葉大學', '小葉大學'

thegrid = GridSpec(5, 5, width_ratios=[1, 0.1, 1, 0.1, 1], height_ratios=[1, 0.22, 1, 0.22, 1])
pl.subplot(thegrid[0, 0])
value3 = [77, 83]
pa, pb = pl.bar(labels, value3)
pa.set_facecolor('lightcoral')
pb.set_facecolor('lightskyblue')
pl.title('註冊率(%)')

pl.subplot(thegrid[0, 2])
value4 = [767, 483]
pa, pb = pl.bar(labels, value4)
pa.set_facecolor('lightcoral')
pb.set_facecolor('lightskyblue')
pl.title('學生數')

pl.subplot(thegrid[0, 4])
value5 = [55, 63]
pa, pb = pl.bar(labels, value5)
pa.set_facecolor('lightcoral')
pb.set_facecolor('lightskyblue')
pl.title('最低錄取分數')

pl.subplot(thegrid[2, 0])
value6 = [234, 189]
pa, pb = pl.bar(labels, value6)
pa.set_facecolor('lightcoral')
pb.set_facecolor('lightskyblue')
pl.title('科系經費(萬)')

pl.subplot(thegrid[2, 2])
value7 = [13, 16]
pa, pb = pl.bar(labels, value7)
pa.set_facecolor('lightcoral')
pb.set_facecolor('lightskyblue')
pl.title('就業比率(%)')

pl.subplot(thegrid[2, 4])
value8 = [20, 22]
pa, pb = pl.bar(labels, value8)
pa.set_facecolor('lightcoral')
pb.set_facecolor('lightskyblue')
pl.title('就業平均薪資(千)')

pl.subplot(thegrid[4, 0])
value9 = [10, 12]
pa, pb = pl.bar(labels, value9)
pa.set_facecolor('lightcoral')
pb.set_facecolor('lightskyblue')
pl.title('科系相關大公司就業比率(%)')

pl.subplot(thegrid[4, 2])
value10 = [77, 63]
pa, pb = pl.bar(labels, value10)
pa.set_facecolor('lightcoral')
pb.set_facecolor('lightskyblue')
pl.title('考碩班比率(%)')

pl.savefig('02.jpg')
Image.open('02.jpg').show()
pl.gcf().clear()
'''
'''
value = [1, 2, 3, 4]
fig, ax = pl.subplots()
labels = '射手', '坦克', '術士', '輔助'
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0)



pl.subplot(thegrid[0, 1], aspect=1)
pl.pie(value, labels=labels, autopct='%1.1f%%', shadow=True)
#ax.pie(value, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90, radius=1.2)
#ax.set(aspect="equal", title='這是測試')
#pl.show()

'''

'''
fig, bx = pl.subplots()
x = ['專案一',  '專案二', '專案三', '專案四']
high = [45, 52, 60, 77]
pl.bar(x, high)
bx.set_title('test')
pl.savefig('02.jpg')
Image.open('02.jpg').show()
'''
