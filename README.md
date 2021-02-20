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