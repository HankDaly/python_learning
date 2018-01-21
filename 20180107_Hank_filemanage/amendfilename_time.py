#-*- coding:utf-8 -*-
#根据操作时间来改变文件的名字
import os
local = os.getcwd()

#后缀
symbol ='_h'
all_name = []
file_list = []
iterms = os.listdir(local)
for it in iterms:
    all_name.append(os.path.join(local,it))
    

s = sorted(all_name,key=lambda d : os.stat(d).st_ctime)

for name in s:
    if os.path.isfile(name):
        file_list.append(name)
            

for file in file_list:
    new_name = str(str(file_list.index(file))+symbol+os.path.splitext(file)[1])
    os.rename(file,os.path.join(os.path.split(file)[0],new_name))
