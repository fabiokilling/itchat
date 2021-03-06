# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 16:27:15 2018

@author: ArcherX
"""
import itchat
itchat.login()
#爬取自己号有相关信息，返回一个json文件
friends = itchat.get_friends(update=True)[0:]
#初始化计数器
male = female = other = 0
#friends[0]是自己的信息，所以要从friends[1]开始
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
#计算朋友总数
total = len(friends[1:])
#打印出自己的好友性别比例
print("男性好友： %.2f%%" %(float(male)/total*100)+"\n"+
      "女性好友： %.2f%%" %(float(female)/total*100)+"\n"+
      "不明性别好友： %.2f%%" %(float(other)/total*100)+"\n"+
      "好友总数：%d"%total)
#定义一个函数，用来爬取各个变量
def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable
#调用函数得到各变量，并把数据存到csv文件中，保存到桌面
NickName = get_var("NickName")
Sex = get_var('Sex')
Province = get_var('Province')
City = get_var('City')
Signature = get_var('Signature')
from pandas import DataFrame
data = {'NickName\t':NickName,'Sex\t':Sex,'Province\t':Province,
        'City\t':City,'Signature\t':Signature}
frame = DataFrame(data)
frame.to_csv('data.csv',index=True)
import re 
siglist = []
for i in friends:
    signature = i["Signature"].strip().replace("span","").replace("class","").replace("emoji","")
    rep = re.compile("1f/d+/w*|[<>/=]")
    signature = rep.sub("",signature)
    siglist.append(signature)
text = "".join(siglist)
import jieba
wordlist = jieba.cut(text,cut_all=True)
word_space_split = " ".join(wordlist)
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
import PIL.Image as Image
coloring = np.array(Image.open("C:/Users/ArcherX/Desktop/pika.jpg"))
stopwords = STOPWORDS.copy()
stopwords.add("输入你想屏蔽的关键词")    #输入你想屏蔽的关键词
my_wordcloud = WordCloud(background_color="white",max_words=2000,
                         mask=coloring,max_font_size=60,random_state=42,scale=8,
                         font_path="C:/ProgramData/Anaconda3/Lib/site-packages/matplotlib/mpl-data/fonts/ttf/msyhbd.ttc").generate(word_space_split)

image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
my_wordcloud.to_file("C:/Users/ArcherX/Desktop/词云03.jpg")
plt.show()
