# pppXray
**作用：**

Xray批量化自动扫描

**使用方法：**

一，在target.txt里按行放置待扫描URL，如图：

![](https://github.com/Cl0udG0d/pppXray/blob/main/images/screen2.png)

二，将Xray所在文件夹配置到电脑环境变量里

三，然后运行pppXray.py即可

**运行截图：**

![](https://github.com/Cl0udG0d/pppXray/blob/main/images/screen.png)

关于[Xray高级版破解](https://www.cnblogs.com/Cl0ud/p/13884206.html)



### 2021/2/20更新

添加命令行参数与自定义`xray`插件用法，可通过 `--help`查看

![](https://github.com/Cl0udG0d/pppXray/blob/main/images/screen3.png)

`-r,--readfile`参数指定批量读取文件名，默认文件名为`target.txt`

![](https://github.com/Cl0udG0d/pppXray/blob/main/images/screen4.png)

`--plugins`参数指定xray插件

如图：

输入 `python3 pppXray.py --plugins cmd_injection -r target.txt`，使用注入插件进行检测

![](https://github.com/Cl0udG0d/pppXray/blob/main/images/screen5.png)



### 2021/5/5更新

看到了黑白某道的公众号文章，这么菜的脚本也能水文章了，xs

但为了方便初学安全的小伙伴更方便使用`xray`，参考之前[花溪九尾](https://github.com/Cl0udG0d/HXnineTails)的经验，在脚本中兼容专业版和社区版，以及添加分类的功能，大伙儿就不用点开每个漏洞报告看了，因为有部分类型的漏洞会被忽略，节省查看报告时间

使用前记得`pip install -r requirements.txt` （没科学上网的自主换源）

![](https://github.com/Cl0udG0d/pppXray/blob/main/images/screen6.png)