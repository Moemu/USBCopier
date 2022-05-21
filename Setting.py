import PySimpleGUI as sg

class Easy_GUI:
    def Text(text,font=('微软雅黑 10')):
        return sg.Text(text,font=font)
    def InputCombo(text,value=None,font=('微软雅黑 10'),size=(6,12)):
        return sg.InputCombo(text,default_value=value,font=font,size=size)
    def FolderBrowse(text,font=('微软雅黑 10')):
        return sg.FolderBrowse(text,font=font)
    def Button(text,font=('微软雅黑 10')):
        return sg.Button(text,font=font)

def read_json():
    import json
    try:
        with open('setting.json','r') as f:
            json_data=json.loads(f.read())
    except:
        write_json('关闭','','600')
        with open('setting.json','r') as f:
            json_data=json.loads(f.read())
    auto_start=json_data['auto_start']
    save_path=json_data['save_path']
    wait_time=json_data['wait_time']
    return auto_start,save_path,wait_time

def auto_start_reg(auto_start):
    import win32api,win32con,os
    try:
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',0, win32con.KEY_ALL_ACCESS)
        if auto_start=='开启':
            win32api.RegSetValueEx(key,'USBCopier',0,win32con.REG_SZ,'{}\\USBCopier.exe'.format(os.getcwd()))#写值（key, '项名', ...）
        else:
            win32api.RegSetValueEx(key,'USBCopier',0,win32con.REG_SZ,'')
    except:
        pass

def write_json(auto_start,save_path,wait_time):
    import json
    if auto_start==None or save_path==None or wait_time==None:
        return None
    setting={
        "auto_start":auto_start,
        "save_path":save_path,
        "wait_time":wait_time
    }
    json_data=json.dumps(setting)
    with open('setting.json','w') as f:
        f.write(json_data)

def main():
    auto_start,save_path,wait_time=read_json()
    layout=[
        [Easy_GUI.Text('开机自启动'),Easy_GUI.InputCombo(['开启','关闭'],auto_start),Easy_GUI.Text('(此操作需要管理员特权)')],
        [Easy_GUI.Text('文件存放路径'),sg.Input(save_path),Easy_GUI.FolderBrowse('打开')],
        [Easy_GUI.Text('等待复制时间'),sg.Input(wait_time)],
        [Easy_GUI.Button('保存')]
    ]
    Setting_GUI=sg.Window('设置页面',layout=layout)
    event,values=Setting_GUI.Read()
    if event==sg.WIN_CLOSED or event=='Exit':
        return None
    print(values)
    auto_start=values[0]
    auto_start_reg(auto_start)
    save_path=values[1]
    wait_time=values[2]
    write_json(auto_start,save_path,wait_time)

if __name__=='__main__':
    main()