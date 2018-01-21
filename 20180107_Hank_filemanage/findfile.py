# -*- coding:utf-8 -*-
import os

filename = input('输入想要查找的文件名')
filelist = []
local = os.getcwd()
def find_file(address,filename):
    fn = filename
    ad = address
    for x in [x for x in os.listdir(ad)]:
        file_name = os.path.join(ad,x)
        if os.path.isdir(file_name):
            find_file(file_name,fn)
        elif os.path.isfile(file_name):
            name = os.path.split(file_name)
            if name[1].find(fn) != -1:
                filelist.append(file_name)
        else:
            print('this' + file_name)


find_file(local,filename)
print(filelist)
input('')
