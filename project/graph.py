# -*- coding: utf-8 -*-
import matplotlib.pyplot as pl
pl.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
pl.rcParams['font.serif'] = ['Microsoft JhengHei']
from matplotlib.gridspec import GridSpec
import numpy
from PIL import Image


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
