# itchat

对接个人微信，使用python模块达成各种功能

在运行时候，大多数人会在词云wordcloud这个模块出现报错，安装不上，解决方法如下博客

https://blog.csdn.net/u012942818/article/details/75144001

在运行的时候填写路径，按照WIN10的属性，复制的路径为C:\Users\ArcherX\Desktop\wechat.jpg
运行代码后会报错
报错信息如下SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
解决方式为，将路径中的\全部改为/


运行报错OSError: cannot open resource

很明显的字体文件找不到位置，python的报错好容易看懂的说。
解决中!!
PIL无法定位到字体文件的位置，可以进行以下操作：


1、进入python的安装目录，一般默认是C:\python27
(我的是在Anaconda3里C:\ProgramData\Anaconda3）

2、搜索.ttf


3、即可查到自己的电脑有哪些中字体格式，然后随机选一种并把绝对路径替换到代码中的Arial.ttf即可


例如：我查找到的绝对路径是：C:\ProgramData\Anaconda3\Lib\site-packages\matplotlib\mpl-data\fonts\ttf\cmb10.ttf

所以要把\改成/，混蛋为什么我电脑会这样。
(突然想起来，其实很简单啊，我使用的是spyder，然后瞎按，一般我以为是Ctrl+F就能解决，但是查找里面没有替换功能，然后按到了Ctrl+R发现可以了，在
搜索栏里面输入符号\，然后再在Replace with：里面输入符号/，点击Replace all就可以一次性全部替换了）。。话说写这段话我老是想按Tab补全拼写，入迷了。。


基本上到这里运行的所有的坑都填完了，然后的话，还修改了两次代码，发现显示的词云图片效果很不理想，原因是wordcloud这个模块学习的太少，花了几分钟去看文档快速入门改参数去咯。生成的两张图就不放上来啦，话说能放吧应该。。以前在tapd上放图好简单，因为模块化了。


完成咯，不想再贴修改过程了，直接放最终代码。哈哈



突然发现，全部的\改为/之后，前面的\t \n全部被改了，怪不得某次运行代码后，输出会不换行。




未完待续...
