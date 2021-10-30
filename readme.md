# 隐藏式U盘文件复制器

## 声明

请<u>不要</u>使用此程序复制**隐私文件**（例如：**国家机密和其他个人隐私信息等**），本程序**仅**能在**被复制U盘的所有者同意后且被复制U盘只能为学习资料**的情况下使用，使用本程序则说明您同意此条款，**由用户使用该程序后出现的违法违规和违背道德准则的情况，作者概不负责，使用者需承担相应的法律责任**

本程序适用环境：**在老师允许的情况下复制老师U盘中的学习文档**

## 前言

使用该程序前用户必须阅读上面的声明才能使用本程序，建议在Windows 10 x64的系统下运行

## 使用

阅读并同意此条款后，从[Releases](https://github.com/WhitemuTeam/USBCopyer/releases)中下载`USBCopier.exe`，双击运行后程序会在后台运行，等待插入U盘（每隔30s检查磁盘情况），插入U盘后的10分钟后才会开始复制文件（此举是为了防止在读取或使用U盘文件时出现卡顿），届时程序会在一瞬间弹出一个cmd窗口，复制结束后程序会等待拔出U盘并再次等待插入U盘，复制后的文件在files文件夹中，可使用Stop.bat停止本程序后台进程

## 原理

首次启动会创建一个files文件夹用于存放文件并读取磁盘信息，获取当前分区数量，并进入等待循环，在此循环中，插入U盘前每1s检查一次分区情况，一旦发现有新分区则会获取新分区的盘符并等待10分钟，然后程序会生成一个copy.bat，bat中写入隐藏cmd窗口的指令和复制命令，然后程序会运行这个copy.bat并开始复制文件，复制结束后移除copy.bat，随后程序进入等待循环，当拔出U盘后，此时程序会重新获取分区信息并继续进入等待循环，等待下一次U盘插入（具体看源码，这里说不清）

## 目录文件

### LOGO.ico

`USBCopier.exe`的图标，可删除

### Readme.md

本文档，**阅读并同意本文档中的条款**后可删除

### Stop.bat

用于关闭`USBCopier.exe`的后台进程，可直接运行

### USBCopier.exe

（您需要到[Releases](https://github.com/WhitemuTeam/USBCopyer/releases)中获取）

主程序，同意条款后可直接运行

### USBCopier.py

`USBCopier.exe`的Python源码文件，在安装并配置Python环境且同意条款后可运行

### *Copy.bat

程序运行时生成的文件，用于隐藏式复制U盘文件，会自动删除

### setting.json

设置，里面的参数'wait'代表等待时间（每次获取分区数的间隔时间），以秒作为单位，默认为1，若删除此文件则使用默认参数(max=1)

## 后话

许可证：[Apache-2.0 License](https://github.com/WhitemuTeam/USBCopyer/blob/main/LICENSE)

未经允许不可转载

联系方式：WhitemuTeam@outlook.com

WhitemuTeam