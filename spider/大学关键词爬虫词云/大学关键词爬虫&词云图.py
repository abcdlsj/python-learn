import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import jieba
import bs4  # 要使用bs4.element.Tag
from wordcloud import WordCloud, ImageColorGenerator  # 引入词云
from PIL import Image
import numpy as np


def get(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""


def fill(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[1].string, tds[3].string])


def printf(ulist, num):
    print("{:^10}{:^10}".format("学校", "得分"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}{:^10}".format(u[0], u[1]))
        n=float(u[1])
        m=int(n)
        file_abs = "C:\\Users\\70706\\Desktop\\date.txt"  # 将大学排名放入一个文件里面
        with open(file_abs, "a")as f:
           for k in range(m):
               f.write(u[0])
def cloud():
    text = open("C:\\Users\\70706\\Desktop\\date.txt","rb").read()
    wordlist = jieba.cut(text, cut_all=False)
    wl = " ".join(wordlist)
    text_mask = np.array(Image.open("C:\\Users\\70706\\Desktop\\im1.jpg"))
    #text_mask= plt.imread('C:\\Users\\70706\\Desktop\\hfut.jpg')
    image_colors = ImageColorGenerator(text_mask)
    wc = WordCloud(font_path="C:\\Windows\\Fonts\\fangsong_GB2312.ttf",  # 设置字体为仿宋,默认字体不识别汉字
                   mask=text_mask,
                   #width=8000,height=6000,
                   background_color="white",
                   max_words=20000,  # 设置最大显示的字数
                   max_font_size=100,  # 设置字体最大值
                   #random_state=400,# 设置有多少种随机生成状态，即有多少种配色方案
                   )
    myword=wc.generate(wl)
    #myword=wc.generate(wl)
    plt.imshow(myword)
    plt.imshow(myword.recolor(color_func=image_colors))
    plt.axis("off")
    plt.show()
    myword.to_file("C:\\Users\\70706\\Desktop\\text.jpg")
def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html#top'
    html = get(url)
    fill(uinfo, html)
    printf(uinfo, 300)
    cloud()
main()
