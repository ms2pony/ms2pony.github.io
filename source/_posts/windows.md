---
title: windows系统中常见问题
categories: operate
---
# 1   常见和新问题

## 1.1 windows shell

微软官方的windows shell的文档 参考 1https://docs.microsoft.com/zh-cn/windows/win32/shell/shell-entry (该文档的解释让我觉得这是目前我觉得这是windows下==最重要的内容==(写这段的时间为20211113))

上面的参考资料对windows shell的描述：

> The Windows UI provides users with ==access to a wide variety of objects(1)== necessary for running applications and managing the operating system. The most numerous and familiar of these objects are the folders and files that reside ==on computer disk drives(2)==. There are also a number of virtual objects that allow the user to ==perform tasks such as sending files to remote printers or accessing the Recycle Bin(3)==. The Shell organizes these objects into ==a hierarchical namespace(4)== and provides users and applications with a consistent and efficient way to ==access and manage objects(5)==.

上面引用，我做了一些笔记，

1. 高亮1说windows提供的UI让用户可以访问很多对象，这些对象对正在运行的应用和管理系统十分重要
2. 高亮2说高亮1提到的对象大多数都驻留在硬盘中
3. 高亮3说上面提到的对象是虚拟对象，这些虚拟对象能够执行一些远程打印和访问回收站等任务
4. 高亮4和5说明shell把这些对象组织到一个分层命名空间中，并未用户和应用程序提供高效的方法来管理和访问这些对象

2021年11月24日00:12:57

## 1.2 快捷方式的疑问

快捷方式就是一个普通的文件，里面的内容是二进制的，系统是怎么识别这个文件是快捷方式的呢，特别特别粗暴简单，就是名字后缀是`.lnk`的文件，就会被识别为快捷方式文件，除此之外快捷方式和普通文件没有任何的区别。

你也可以随便创建一个文件，**只要名字是`.lnk`就行的，创建完了之后，windows的资源管理器会自动过滤`.lnk`后缀，**你想要消除文件名的`.lnk`后缀，就需要借助非windows的工具来对文件进行操作。比如使用python操作

## 1.3 windows的文件属性介绍

相比于unix系统下文件的属性，windows下的文件属性是比较简单的，如下：

![windows-aa.png](https://raw.githubusercontent.com/ms2pony/ms2pony.github.io/master/source/_posts/img/1637416251103.png)

可以看到充其量，windows文件就7个属性

## 1.4 解决某个文件已经在另一个程序中打开

![windows-ab.png](https://raw.githubusercontent.com/ms2pony/ms2pony.github.io/master/source/_posts/img/1637235939766.png)

参考 https://blog.csdn.net/qq_21808961/article/details/81192410

## 1.5 重新启动资源管理器

打开任务管理器->任务->新建任务，输入任务`explorer.exe`

参考 https://jingyan.baidu.com/article/48206aeadd044a216bd6b341.html k 这时候我们在任务管理器窗口中，选择文件菜单新建任务

## 1.6 导航页被篡改
参考：https://blog.csdn.net/weixin_46891900/article/details/105985983 k 找到浏览器图标，右键，点击属性，别忘了把只读上的✓关掉

## 1.7 WSL

与wmware不兼容，关闭了之后再重启，可能需要该命令：`bcdedit /set hypervisorlaunchtype auto`

参考：https://blog.csdn.net/weixin_43271225/article/details/115698940

又想关闭Wsl，使用wmware时，关闭下列功能：

![windows-ac.png](https://raw.githubusercontent.com/ms2pony/ms2pony.github.io/master/source/_posts/img/1631521696891.png)

![windows-ad.png](https://raw.githubusercontent.com/ms2pony/ms2pony.github.io/master/source/_posts/img/1631521710318.png)



并使用该命令：`bcdedit /set hypervisorlaunchtype off`

## 1.8 快捷方式和软链接区别

target改名后软链接

## 1.9 vs无法调试

![windows-ae.png](https://raw.githubusercontent.com/ms2pony/ms2pony.github.io/master/source/_posts/img/1631373977956.png)

运行库选择MTD即可


## 1.10 设置默认浏览器

更改打开链接时的浏览器

关键词：win+默认应用

参考：https://jingyan.baidu.com/article/86112f1379042927379787b7.html

## 1.11 包管理器

Chocolatey，Scoop；Chocolatey简单，Scoop自定义程度高
参考：https://zhuanlan.zhihu.com/p/128955118 概述：仅仅是简单介绍安装和使用
参考：https://docs.chocolatey.org/en-us/  概述：官方文档，介绍gui版本，cli版本；可读性不错

参考：https://community.chocolatey.org/packages 社区维护的package

总结：

CLI版有bug，GUI版本(chocolatey gui)方便又好用

1. `choco upgrade [package_name]`更新

2. `choco install[package_name]`安装

3. `choco uninstall [package_name]`卸载

4. **不足：**`choco list`等其他命令会卡在那里不动
5. `choco outdated` 查看可升级版本

## 1.12 ISO打开方式
.ISO格式的文件，想打开使用资源管理器打开，关闭时弹出

![windows-af.png](https://raw.githubusercontent.com/ms2pony/ms2pony.github.io/master/source/_posts/img/1631346547141.png)

# 2 MFC

参考 https://www.bilibili.com/video/BV1QA411g7dX (B站视频)

相关vs项目代码在`G:\iii\ii\i\workStudation\Studation\MFC`中

注意MFC和win32工程最好创建后都设置成多字节字符集：

![windows-ag.png](https://raw.githubusercontent.com/ms2pony/ms2pony.github.io/master/source/_posts/img/1637692442759.png)

## 2.1 常用的头文件
`afx.h`-将各种MFC头文件包含在内
`afxwin.h`-包含各种MFC窗口类，包含了`afx.h`和`windows.h`
`afxext.h`-提供了扩展窗口类的支持，例如工具栏，状态栏等

## 2.2 MFC与win32程序区别

可以调MFC库就称为MFC程序反之为win32程序

## 2.3 MFC控制台程序

1. 与win32控制台程序的差别

   - main函数不同于普通的控制台程序

     `int _tmain(int argc, TCHAR* arg[], TCHAR* envp[])`比起win32的`main`多了一个环境变量参数

   - `CWinApp theApp`这行代码，比起win32多了一个全局对象

2. 经验之谈

   - 以Afx开头可以确定为MFC库中的全局函数，全局函数指独立于类的函数

     ![windows-ah.png](https://raw.githubusercontent.com/ms2pony/ms2pony.github.io/master/source/_posts/img/1637686772998.png)

   - 以::开头可以确定为win32的API函数，`::`开头是因为默认空间是win32API空间

     ![windows-ai.png](https://raw.githubusercontent.com/ms2pony/ms2pony.github.io/master/source/_posts/img/1637686679058.png)

## 2.4 MFC库程序

1. MFC静态库

2. MFC动态库

   - 使用静态MFC库制作自己的动态库
   - 使用动态MFC库制作自己的动态库

   两者切换操作如下：

   ![windows-aj.png](https://raw.githubusercontent.com/ms2pony/ms2pony.github.io/master/source/_posts/img/1637687415284.png)

3. 扩展库

   规则库可以被各种程序所调用，==扩展库只能被MFC程序调用==

## 2.5 MFC窗口程序

1. 单文档视图架构程序(single document)

   - CWinApp-应用程序类，负责管理应用程序的流程

   - CFrameWnd-框架窗口类，负责管理框架窗口
   - CView-视图窗口类，负责显示数据
   - CDocument-文档类，负责管理数据

2. 多文档视图架构程序

   - CMDIFrameWnd-多文档主框架窗口类

   - CMDIChildWnd-多文档子框架窗口类

     可以看到下面有两个窗口：

     ![windows-ak.png](https://raw.githubusercontent.com/ms2pony/ms2pony.github.io/master/source/_posts/img/1637689887959.png)
     
   - 其他类与单文档视图架构程序类似

3. 对话框应用程序

   什么是对话框？程序运行起来，出现的第一个界面就是对话框

## 2.6 MFC库中相关类简介

1. CObject类

   - MFC类库中绝大部分类的父类，提供了MFC类库中一些基本的机制
   - 对运行时类信息的支持
   - 对动态创建的支持
   - 对序列化的支持

2. CWinApp类

   应用程序类，封装了应用程序、线程等信息

3. CDocument类，文档类，管理数据
4. Frame Windows 框架窗口类，封装了窗口程序组成的各种框架窗口
5. CSplitterWnd-用来完成拆分窗口的类
6. Control Bars-控件条类

还有很多，不列举了

## 2.7 小实验：将win32程序转化为MFC程序

分为两步：

1. 加上头文件，<afxwin.h>
2. setting当中设置使用MFC库

总结：win32程序和MFC程序区别仅仅为能不能使用MFC而已

## 2.8 part2

ps：前面2.1-2.7都是我第一天所学内容，==算是part1了，只是我懒得排版==，先就这样，2021年11月26日16:06:28

### 入口函数

与win32窗口程序相同，都是从WinMain入口。但是MFC库已经实现了WinMain函数，这意味着==MFC会自动安排程序的流程(因为它在组织入口函数)==

### 执行流程

启动，然后会先构造theAPP对象，这个对象的声明和构造函数的定义由我们来写

# 3   windows平台开发程序的三种方式

![windows-al.png](https://raw.githubusercontent.com/ms2pony/ms2pony.github.io/master/source/_posts/img/1631374115511.png)

## 3.1 消息的来源

![windows-am.png](https://raw.githubusercontent.com/ms2pony/ms2pony.github.io/master/source/_posts/img/1631374190402.png)

## 3.2 消息结构

![windows-an.png](https://raw.githubusercontent.com/ms2pony/ms2pony.github.io/master/source/_posts/img/1631374240816.png)

## 3.3 实现过程

![windows-ao.png](https://raw.githubusercontent.com/ms2pony/ms2pony.github.io/master/source/_posts/img/1631374300177.png)

## 3.4 代码

### 3.4.1 PreTranslateMessage

不处理异步方式，PostMessage函数为同步方式，

### 3.4.2 WindowProc

我处理异步方式，SendMessage函数为异步方式

# 4   windows 网络编程

## 4.1 网络程序架构和套接字的类型

![windows-ap.png](https://raw.githubusercontent.com/ms2pony/ms2pony.github.io/master/source/_posts/img/1631457768392.png)

B/S 浏览器和服务器 C/S服务端和客户端

![windows-aq.png](https://raw.githubusercontent.com/ms2pony/ms2pony.github.io/master/source/_posts/img/1631457796945.png)

ICMP协议是原始套接字，ping由ICMP协议实现

![windows-ar.png](https://raw.githubusercontent.com/ms2pony/ms2pony.github.io/master/source/_posts/img/1631457903202.png)

# 5  windows中的专有名词

## 5.1 WMI

WMI（Windows Management Instrumentation,Windows 管理规范）是一项核心的 Windows 管理技术；用户可以使用 WMI 管理本地和远程计算机。

# 6  工具推荐

压缩软件：7z

winhex

查看硬盘数据及修改硬盘数据

