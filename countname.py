import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread
from PIL import Image

    # 此函数用于绘制条形图
def showNameBar(name_list_sort,name_list_count):
    # x代表条形数量
    x = np.arange(len(name_list_sort))
        # 处理中文乱码
    plt.rcParams['font.sans-serif'] = ['SimHei']
        # 绘制条形图，bars相当于句柄
    bars = plt.bar(x,name_list_count)
        # 给各条形打上标签
    plt.xticks(x,name_list_sort)
    plt.xlabel('人物')
    plt.ylabel('次数')
        # 显示各条形具体数量
    i = 0
    for bar in bars:
        plt.text((bar.get_x() + bar.get_width() / 2), bar.get_height(), '%d' % name_list_count[i], ha='center', va='bottom')
        i += 1
        # 显示图形
    plt.show()
def Ciyun(g):
    coloring = np.array(Image.open("D:/py/四大名著/love.jpg")) #图片路径自己改
    wc = WordCloud( font_path='C:/Windows/Font/simfang.ttf',#设置字体  
                    background_color="white", #背景颜色  
                    max_words=2000,# 词云显示的最大词数  
                    mask=coloring,#设置背景图片  
                    max_font_size=50, #字体最大值  
                    random_state=42,  
                    ).generate(g)
    image_colors = ImageColorGenerator(coloring)
    plt.figure(figsize=(64,32))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis('off')
    plt.show()




